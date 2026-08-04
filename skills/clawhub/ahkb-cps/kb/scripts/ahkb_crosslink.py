"""
ahkb_crosslink.py — 知识链构建引擎（主匹配引擎）
功能：对知识元、 .ctx 资源、原始文件进行关联，分3步完成：
  1. 知识元 - 知识元：名称硬关联、TF-IDF 语义匹配，自动补齐 [[链接]]，消除孤立知识元
  2. 知识元 - 资源：TF-IDF 匹配 + 加权评分，双向写入：
     - .ctx 的 belongs_to ← 知识元
     - 知识元的 resources + 正文 ![[引用]] ← .ctx
  3. 知识元 - 原始文件: TF-IDF 语义匹配，标明知识来源
"""
import os, sys, re, json, datetime, threading, time
from pathlib import Path
import jieba
import jieba.analyse
import platform
from ahkb_chunks import load_all_chunks_with_text, load_chunk_index
from ahkb_chunk_match import match_unit_to_chunks, write_related_files_to_unit, build_related_files_section, get_chunk_matching_stats
from ahkb_trash import _trash_file, _trash_dir
if platform.system() == "Windows":
	try:
		import ctypes
		kernel32 = ctypes.windll.kernel32
		kernel32.SetConsoleMode(kernel32.GetStdHandle(-11), 7)
	except Exception:
		pass

# ─── 暂停控制 ───
_PAUSE_FLAG = [False]
# ─── GUI 授权锁：只有 ahkb.py 的 GUI 窗口才能调用 cross_link() ───
_GUI_AUTHORIZED = False

# ─── 心跳状态（方案C：智能进度JSON） ───
_HB = {
	"phase": "starting",
	"phase_name": "启动中",
	"current": 0,
	"total": 1,
	"detail": "",
	"start_time": 0,
}
_HB_LOCK = threading.Lock()

# ─── detached 模式文件 IPC（解决大模型超时截断问题） ───
_PROGRESS_FILE = None     # 进度文件路径（_crosslink_progress.json）
_RESULT_FILE = None       # 结果文件路径（_crosslink_result.json）
_PID_FILE = None          # PID 文件路径（_crosslink.pid）
_CROSSLINK_WS = None      # 工作空间路径（回收站需要）
_IS_DETACHED_CHILD = False

def _init_detached_files(workspace):
	"""初始化 detached 模式的文件路径。"""
	global _PROGRESS_FILE, _RESULT_FILE, _PID_FILE, _CROSSLINK_WS
	_CROSSLINK_WS = Path(workspace)
	tmp_dir = _CROSSLINK_WS / "临时工作文件"
	tmp_dir.mkdir(parents=True, exist_ok=True)
	_PROGRESS_FILE = tmp_dir / "_crosslink_progress.json"
	_RESULT_FILE = tmp_dir / "_crosslink_result.json"
	_PID_FILE = tmp_dir / "_crosslink.pid"

def _is_pid_alive(pid):
	"""跨平台检查 PID 是否存活。"""
	import platform as _plat
	try:
		if _plat.system() == "Windows":
			import ctypes as _ct
			k32 = _ct.windll.kernel32
			handle = k32.OpenProcess(0x0400, False, pid)
			if handle:
				k32.CloseHandle(handle)
				return True
		else:
			os.kill(pid, 0)
			return True
	except (OSError, Exception):
		pass
	return False

def _write_detached_pid():
	"""写入 PID 文件。"""
	if _PID_FILE:
		_PID_FILE.write_text(json.dumps({
			"pid": os.getpid(),
			"started_at": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
		}, ensure_ascii=False), encoding="utf-8")

def _cleanup_detached_pid():
	"""将 PID 文件移入回收站。"""
	if _PID_FILE and _PID_FILE.exists() and _CROSSLINK_WS:
		_trash_file(_PID_FILE, _CROSSLINK_WS)

def _write_detached_result(status, **kwargs):
	"""写入 detached 模式的结果文件。"""
	if not _RESULT_FILE:
		return
	result = {"status": status}
	result.update(kwargs)
	try:
		_RESULT_FILE.write_text(json.dumps(result, ensure_ascii=False), encoding="utf-8")
	except Exception:
		pass

def _heartbeat_worker(stop_event, interval=10):
	"""心跳线程：每 interval 秒输出结构化 JSON 进度。
	在 detached 模式下，同时写入 _crosslink_progress.json 供 LLM 轮询。"""
	start = time.time()
	def _write():
		with _HB_LOCK:
			phase = _HB["phase"]
			pname = _HB["phase_name"]
			cur = _HB["current"]
			tot = _HB["total"]
			detail = _HB["detail"]
		elapsed = int(time.time() - start)
		msg = {
			"heartbeat": "alive",
			"phase": phase,
			"phase_name": pname,
			"done": cur,
			"total": tot,
			"pct": round(cur / max(tot, 1) * 100, 1) if tot else 0,
			"elapsed_seconds": elapsed,
		}
		if detail:
			msg["detail"] = detail
		# detached 模式：写入进度文件供 LLM 轮询
		if _PROGRESS_FILE:
			try:
				msg_file = dict(msg)
				msg_file["status"] = "running"
				msg_file["last_update"] = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
				_PROGRESS_FILE.write_text(json.dumps(msg_file, ensure_ascii=False), encoding="utf-8")
			except Exception:
				pass
	# 立即写入初始进度，确保 LLM 首次轮询就能看到
	_write()
	while not stop_event.wait(interval):
		_write()

def _hb_update(phase=None, phase_name=None, current=None, total=None, detail=None):
	"""线程安全地更新心跳状态。"""
	with _HB_LOCK:
		if phase is not None:
			_HB["phase"] = phase
		if phase_name is not None:
			_HB["phase_name"] = phase_name
		if current is not None:
			_HB["current"] = current
		if total is not None:
			_HB["total"] = total
		if detail is not None:
			_HB["detail"] = detail

def _check_pause():
	"""检查暂停标记，若暂停则循环等待直到恢复。"""
	while _PAUSE_FLAG[0]:
		time.sleep(0.3)

def _safe_write_text(filepath, content, retries=3):
	"""安全写入文件：用临时文件+原子替换绕过 Obsidian 等软件的文件锁。
	返回 True 表示写入成功，False 表示失败。"""
	for _retry in range(retries):
		try:
			_tmp = filepath.with_suffix(filepath.suffix + ".tmp") if isinstance(filepath, Path) else Path(filepath).with_suffix(Path(filepath).suffix + ".tmp")
			_tmp.parent.mkdir(parents=True, exist_ok=True)
			_tmp.write_text(content, encoding="utf-8")
			os.replace(_tmp, filepath)
			return True
		except (OSError, PermissionError):
			if _retry < retries - 1:
				time.sleep(0.5)
	return False

def _extract_ctx_tags(content):
	"""从 .ctx 文件内容中提取 tags 字符串"""
	fm = content.split("---", 2)[1] if content.startswith("---") else content
	m = re.search(r'^tags:\s*\[(.*?)\]', fm, re.MULTILINE)
	return m.group(1) if m else ""

def _extract_ctx_importance(content):
	"""从 .ctx 文件内容中提取 importance 值"""
	m = re.search(r'^importance:\s*(\d+)', content, re.MULTILINE)
	return int(m.group(1)) if m else 3

def _extract_ctx_user_edited(content):
	"""从 .ctx 文件内容中提取 user_edited 状态"""
	return 1 if "user_edited: true" in content else 0

def _load_weights(workspace):
	"""从 project_settings.json 加载权重配置，不存在则用默认值自动创建。"""
	p = Path(workspace) / "系统设置" / "project_settings.json"
	defaults = {"cContext": 0.5, "cTags": 0.5, "cStars": 0.5, "cEdited": 0.5, "cGranularity": 0.5, "cTextAmount": 0.5, "cLinksNum": 0.5, "cLinksDensity": 0.5}
	if p.exists():
		try:
			data = json.loads(p.read_text(encoding="utf-8"))
			for k in defaults:
				if k in data.get("weights", {}):
					defaults[k] = float(data["weights"][k])
		except:
			pass
	else:

		# 自动创建默认权重文件
		try:
			p.parent.mkdir(parents=True, exist_ok=True)
			p.write_text(json.dumps({"weights": defaults}, ensure_ascii=False, indent=2), encoding="utf-8")
		except:
			pass
	return defaults

def _tags_similarity(ctx_tags_str, unit_text):
	"""计算资源 tags 与知识元内容的关键词相似度（0~1）"""
	if not ctx_tags_str.strip():
		return 0.0
	tags = [t.strip() for t in ctx_tags_str.split(",") if t.strip()]
	if not tags:
		return 0.0
	text_lower = unit_text.lower()
	hits = sum(1 for t in tags if t.lower() in text_lower)
	return hits / len(tags)

def _shorten(name, limit=20):
	if len(name) <= limit:
		return name
	half = limit // 2 - 1
	return name[:half] + '...' + name[-half:]

def _tfidf_similarity(text_a, text_b):
	"""用 jieba TF-IDF 计算两段中文文本的余弦相似度"""
	if not text_a.strip() or not text_b.strip():
		return 0.0
	tags_a = dict(jieba.analyse.extract_tags(text_a, topK=80, withWeight=True))
	tags_b = dict(jieba.analyse.extract_tags(text_b, topK=80, withWeight=True))
	all_words = set(tags_a.keys()) | set(tags_b.keys())
	if not all_words:
		return 0.0
	vec_a = [tags_a.get(w, 0.0) for w in all_words]
	vec_b = [tags_b.get(w, 0.0) for w in all_words]
	dot = sum(va * vb for va, vb in zip(vec_a, vec_b))
	norm_a = sum(v * v for v in vec_a) ** 0.5
	norm_b = sum(v * v for v in vec_b) ** 0.5
	if norm_a == 0 or norm_b == 0:
		return 0.0
	return dot / (norm_a * norm_b)

def _build_tfidf_vector(text):
	"""预提取文本的 TF-IDF 关键词向量，返回 {word: weight} 字典。"""
	text = text.strip()
	if not text:
		return {}
	return dict(jieba.analyse.extract_tags(text, topK=80, withWeight=True))

def _vec_cosine(vec_a, vec_b):
	"""计算两个预提取的 TF-IDF 向量的余弦相似度。"""
	if not vec_a or not vec_b:
		return 0.0
	all_words = set(vec_a.keys()) | set(vec_b.keys())
	if not all_words:
		return 0.0
	a_list = [vec_a.get(w, 0.0) for w in all_words]
	b_list = [vec_b.get(w, 0.0) for w in all_words]
	dot = sum(va * vb for va, vb in zip(a_list, b_list))
	norm_a = sum(v * v for v in a_list) ** 0.5
	norm_b = sum(v * v for v in b_list) ** 0.5
	if norm_a == 0 or norm_b == 0:
		return 0.0
	return dot / (norm_a * norm_b)

def _title_bigram_sim(title_a, title_b):
	"""计算两个知识元名称的字符 bigram 杰卡德相似度"""
	if not title_a or not title_b:
		return 0.0
	a_bigrams = set(title_a[i:i+2] for i in range(len(title_a)-1))
	b_bigrams = set(title_b[i:i+2] for i in range(len(title_b)-1))
	if not a_bigrams or not b_bigrams:
		# 单字符名称，用 unigram
		a_bigrams = set(title_a)
		b_bigrams = set(title_b)
	inter = len(a_bigrams & b_bigrams)
	union = len(a_bigrams | b_bigrams)
	return inter / max(union, 1)

# 终端颜色
G = chr(27) + "[32m"  # 绿色
B = chr(27) + "[94m" # 亮蓝
Y = chr(27) + "[93m" # 黄色
W = chr(27) + "[96m" # 亮青
RD = chr(27) + "[91m" # 亮红
R = chr(27) + "[0m"  # 重置

def _dedup_fm_tags(match):
    """去重 frontmatter tags 数组，保留顺序"""
    prefix = match.group(1)
    tags_str = match.group(2)
    suffix = match.group(3)
    if not tags_str.strip():
        return match.group(0)
    seen = set()
    unique = []
    for tag in tags_str.split(","):
        t = tag.strip()
        if t and t not in seen:
            seen.add(t)
            unique.append(t)
    if len(unique) == len([t.strip() for t in tags_str.split(",") if t.strip()]):
        return match.group(0)
    return prefix + ", ".join(unique) + suffix

def _dedup_body_tags(match):
    """去重正文底部 #tags 行，保留顺序"""
    header = match.group(1)
    tags_line = match.group(2)
    seen = set()
    unique = []
    for tag in tags_line.split():
        t = tag.strip()
        if t and t not in seen:
            seen.add(t)
            unique.append(t)
    if len(unique) == len(tags_line.split()):
        return match.group(0)
    return header + " ".join(unique)

def _dedup_clean(units_dir):
    """标签去重 + resources字段清理 + 格式修复，仅统计有实质修改的文件"""
    stat_tag_fm = 0
    stat_tag_body = 0
    stat_res = 0
    fixed_count = 0
    for f in units_dir.glob("*.md"):
        try:
            orig_raw = f.read_text(encoding="utf-8", errors="ignore")

            # 用副本预处理修复 --- 位置，原稿保留用于对比
            orig = orig_raw
            orig = re.sub(r'^---([^\n])', r'---\n\1', orig)
            orig = re.sub(r'([^\n])---(\n|$)', r'\1\n---\n', orig, count=1)
            fm_match = re.match(r'^---\n(.*?)\n---\n', orig, re.DOTALL)
            if not fm_match:
                continue
            fm = fm_match.group(1).strip()
            body = orig[fm_match.end():]
            changed = False
            has_dedup = False  # 是否发生了实质性修复（去重）

            # 统一 tags 格式：将 tags: "a, b, c" 转为 tags: [a, b, c]
            _tags_str_m = re.match(r'^tags:\s*"([^"]*)"\s*$', fm, re.MULTILINE)
            if _tags_str_m:
                _raw = _tags_str_m.group(1).strip()
                _items = [t.strip() for t in _raw.split(",") if t.strip()]
                if _items:
                    fm = re.sub(
                        r'^tags:\s*"[^"]*"\s*$',
                        'tags: [' + ", ".join(_items) + "]",
                        fm,
                        flags=re.MULTILINE
                    )
                    changed = True
                    has_dedup = True

            # dedup frontmatter tags
            fm_new = re.sub(
                r"(tags:\s*\[)(.*?)(\])",
                lambda m: _dedup_fm_tags(m),
                fm
            )
            if fm_new != fm:
                stat_tag_fm += 1
                fm = fm_new
                changed = True
                has_dedup = True

            # remove empty resources: [] before real resources:, or dangling resources:
            fm_new = re.sub(r'\nresources:\s*\[\]', '', fm)
            if fm_new != fm:
                stat_res += 1
                fm = fm_new
                changed = True

            # dedup body #tags
            body_new = re.sub(
                r'(##\s*标签\n*)((?:#[^\s]+\s*)+)',
                lambda m: _dedup_body_tags(m),
                body
            )
            if body_new != body:
                stat_tag_body += 1
                body = body_new
                changed = True
                has_dedup = True

            # remove extra --- in body head
            body_clean = body
            while body_clean.startswith("---"):
                body_clean = body_clean[3:].lstrip()
                changed = True

            # compress 3+ blank lines
            pre = body_clean
            body_clean = re.sub(r"\n{3,}", "\n\n", body_clean)
            if body_clean != pre:
                changed = True
            pre = fm
            fm = re.sub(r"\n{3,}", "\n\n", fm)
            if fm != pre:
                changed = True

            # 仅当有实质修改时才写入并计数
            new_content = "---\n" + fm.strip() + "\n---\n" + body_clean
            if changed:
                _safe_write_text(f, new_content)
            if has_dedup:
                fixed_count += 1
        except Exception:
            continue
    return {
        "fixed_count": fixed_count,
        "tag_fm": stat_tag_fm,
        "tag_body": stat_tag_body,
        "res_dedup": stat_res,
    }

def cross_link(workspace, verbose=True, dry_run=False):
	"""主匹配引擎。每次执行先清除所有旧连接，再从零匹配。"""
	# ── GUI 守卫：禁止绕过 GUI 直接调用 ──
	if not _GUI_AUTHORIZED:
		import sys as _sys
		_sys.stderr.write("\n" + "!" * 72 + "\n")
		_sys.stderr.write("!!! 错误：cross_link 禁止直接调用！                           !!!\n")
		_sys.stderr.write("!!! 必须通过 ahkb.py maintain 命令执行（会弹出 GUI 窗口）。    !!!\n")
		_sys.stderr.write("!" * 72 + "\n\n")
		_sys.exit(1)
	import sys as _sys
	if verbose:
		_sys.stderr.write(G + "=" * 82 + R + chr(10))
		_sys.stderr.write(G + "     AHKB 知识链构建引擎" + R + chr(10))
		_sys.stderr.write(G + "=" * 82 + R + chr(10))
		_sys.stderr.write(Y + "  本引擎在本地运行，不消耗 Tokens" + R + chr(10))
		_sys.stderr.write(chr(10))
		_sys.stderr.write(G + "  任务一：知识元 ↔ 知识元  — 名称硬关联、TF-IDF 语义加权评分匹配，自动链接" + R + chr(10))
		_sys.stderr.write(G + "  任务二：知识元 ↔ 资源    — TF-IDF 语义加权评分匹配，双向链接" + R + chr(10))
		_sys.stderr.write(G + "  任务三：知识元 ↔ 原始文件 — TF-IDF 语义匹配，标明知识来源" + R + chr(10))
		_sys.stderr.write(chr(10))
		_sys.stderr.write(G + "  处理时间取决于知识元数量和资源数量" + R + chr(10))
		_sys.stderr.write(G + "  正在进行高强度计算，可能需要20分钟或更长时间。请耐心等待，不要中断程序" + R + chr(10))
		_sys.stderr.write(G + "-" * 75 + R + chr(10))
		_sys.stderr.write(chr(10)) 
	# ── 启动心跳线程 ──
	_HB["start_time"] = time.time()
	_hb_stop = threading.Event()
	_hb_thread = threading.Thread(target=_heartbeat_worker, args=(_hb_stop, 30), daemon=True)
	_hb_thread.start()
	_hb_update(phase="cleanup", phase_name="清理旧数据", current=0, total=1, detail="开始清理")
	
	units_dir = Path(workspace) / "知识元"
	resource_base = Path(workspace) / "图片及其他资源"
	if not units_dir.exists() or not resource_base.exists():
		return {"error": "知识元/ 或 图片及其他资源/ 目录不存在"}
	if verbose:
		_sys.stderr.write("   检查知识元格式并去重标签..." + chr(10))
	if not dry_run:
		dedup_result = _dedup_clean(units_dir)
	else:
		dedup_result = {"fixed_count": 0, "tag_fm": 0, "tag_body": 0, "res_dedup": 0}
	cleaned_fake = 0
	cleaned_single_ctx = 0

	# ── 0. 清理资源文件冒充的知识元 ──
	if not dry_run:
		for f in Path(workspace).iterdir():
			if f.is_file() and re.search(r'\.(png|jpg|jpeg|gif|bmp|webp|svg|mp4|mp3|avi|mov|wav)\.[Mm][Dd]$', f.name):
				_trash_file(f, workspace)
				cleaned_fake += 1
				if verbose:
					_sys.stderr.write("   删除了 " + f.name + chr(10))

	# ── 1. 清理单身 .ctx 文件（无对应媒体文件的.ctx）──
	if verbose:
		_sys.stderr.write("   检查单身 .ctx 文件..." + chr(10))
	deleted = []
	if not dry_run:
		for sd in ["images", "videos", "audios", "others"]:
			d = resource_base / sd
			if not d.exists():
				continue
			for f in d.glob("*.ctx"):
				try:
					if os.name == "nt":
						os.chmod(str(f), 0o666)
					content = f.read_text(encoding="utf-8", errors="ignore")
					if re.search(r'remote_url:\s*"http', content) or re.search(r'远程资源[：:]\s*http', content):
						continue
					m = re.search(r'resource_file:\s*"(.+)"', content)
					media_exists = False
					if m:
						media_name = m.group(1)
						media_exists = (d / media_name).exists()
					if not m or not media_exists:
						stem = f.stem
						for ext in ['.png', '.jpg', '.jpeg', '.gif', '.bmp', '.tiff', '.webp',
									 '.mp4', '.avi', '.mov', '.wmv', '.m4v',
									 '.mp3', '.wav', '.aac', '.ogg', '.flac', '.m4a']:
							if (d / (stem + ext)).exists():
								media_exists = True
								break
						if not media_exists:
							for mf in d.iterdir():
								if mf.is_file() and mf.suffix.lower() != '.ctx' and mf.stem == stem:
									media_exists = True
									break
					if not media_exists:
						_trash_file(f, workspace)
						deleted.append(str(f.relative_to(workspace)))
				except Exception:
					# .ctx 文件损坏/不可读
					_trash_file(f, workspace)
	if verbose:
			if deleted:
				_sys.stderr.write("   删除了 " + str(len(deleted)) + " 个单身 .ctx 文件" + chr(10))
			else:
				_sys.stderr.write("   没有需要删除的单身 .ctx 文件" + chr(10))

	# 保存清理计数
	cleaned_single_ctx = len(deleted)
	_hb_update(phase="cleanup", phase_name="清理孤儿资源", current=1, total=5,
	           detail=f"清理了 {cleaned_fake} 个虚假知识元, {cleaned_single_ctx} 个单身 .ctx")

	# ── 2. 扫描没有对应 .ctx 的资源文件 ──
	no_ctx_resources = []
	for sd in ["images", "videos", "audios", "others"]:
		d = resource_base / sd
		if not d.exists():
			continue
		for f in d.iterdir():
			if not f.is_file() or f.suffix.lower() == ".ctx":
				continue
			if not (d / (f.stem + ".ctx")).exists():
				no_ctx_resources.append(f)

	# 自动生成 .ctx 文件
	if not dry_run:
		ctx_content = ""
		for f in no_ctx_resources:
			now_str = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
			rtype = "image" if f.suffix.lower() in ['.png','.jpg','.jpeg','.gif','.bmp','.webp','.svg'] else "other"

			# 自动计算 importance
			imp = 3
			if rtype == "image":
				try:
					from PIL import Image
					with Image.open(f) as _im:
						_s = int((_im.width * _im.height) ** 0.5)
					if _s < 100: imp = 1
					elif _s < 400: imp = 2
					elif _s < 1000: imp = 3
					else: imp = 4
				except:
					pass
			ctx_content = "---" + chr(10)
			ctx_content += "type: resource" + chr(10)
			ctx_content += "resource_type: " + rtype + chr(10)
			ctx_content += "importance: " + str(imp) + chr(10)
			ctx_content += "user_edited: false" + chr(10)
			ctx_content += "last_edited_time: " + now_str + chr(10)
			ctx_content += 'source: ""' + chr(10)
			ctx_content += 'belongs_to_chunk: ""' + chr(10)
			ctx_content += 'chunk_heading: ""' + chr(10)
			ctx_content += 'resource_file: "' + f.name + '"' + chr(10)
			ctx_content += "tags: [待补充]" + chr(10)
			ctx_content += "belongs_to:" + chr(10)
			ctx_content += "---" + chr(10)
			ctx_content += chr(10)
			ctx_content += "![[" + f.name + "]]" + chr(10)
			ctx_content += chr(10)
			ctx_content += "> " + f.stem + chr(10)
			ctx_content += "> " + chr(10)
			ctx_content += "> **注意**：此 .ctx 文件由系统自动生成，**需要用户进一步充实修改**。" + chr(10)
			ctx_content += "> 请补充：来源文档、所属chunk、上下文描述、标签等。" + chr(10)
			ctx_path = f.parent / (f.stem + ".ctx")
			try:
				if os.name == "nt":
					os.chmod(str(ctx_path), 0o666)
				ctx_path.write_text(ctx_content, encoding="utf-8")
			except Exception:
				pass
	if verbose:
		if no_ctx_resources:
			_sys.stderr.write("   发现 " + str(len(no_ctx_resources)) + " 个资源文件没有对应的 .ctx 文件，已自动生成" + chr(10))
		else:
			_sys.stderr.write("   所有资源文件都有对应的 .ctx 文件" + chr(10))

	# ── 2. 清除所有旧连接（每次重新连接） ──
	if not dry_run:
		if verbose:
			_sys.stderr.write("   清除旧链接..." + chr(10))
		for f in units_dir.glob("*.md"):
			try:
				content = f.read_text(encoding="utf-8", errors="ignore")
				new_c = content
				new_c = re.sub(r'\nresources:\n(\s+.*\n?)*', '', new_c)
				new_c = re.sub(r'\n## 关联资源\n.*?(?=\n## |\Z)', '', new_c, flags=re.DOTALL)
				new_c = re.sub(r'\n## 关联知识元\n.*?(?=\n## |\Z)', '', new_c, flags=re.DOTALL)
				new_c = re.sub(r'\n## 关联原始文件\n.*?(?=\n## |\Z)', '', new_c, flags=re.DOTALL)
			# ↑ 删除 AI 在 Phase 1 可能写过的 [[关联知识元]]（AI 必须不写，但 crosslink 以自己为准）
				if new_c != content:
					_safe_write_text(f, new_c)
			except Exception:
				continue
		for subdir in ["images", "videos", "audios", "others"]:
			d = resource_base / subdir
			if not d.exists():
				continue
			for f in d.glob("*.ctx"):
				try:
					if os.name == "nt":
						os.chmod(str(f), 0o666)
					content = f.read_text(encoding="utf-8", errors="ignore")
					new_c = content
					new_c = re.sub(r'\nbelongs_to:\n(\s+-.*\n?)*', '', new_c)
					new_c = re.sub(r'\nbelongs_to:\s*\[\]', '', new_c)
					parts = new_c.split("---", 2)
					if len(parts) >= 3:
						fm = parts[1]; body = parts[2]
						fm = fm.rstrip() + "\nbelongs_to: []"
						new_c = "---" + fm + "\n---" + body
					if new_c != content:
						_safe_write_text(f, new_c)
				except Exception:
					continue
		if verbose:
			_sys.stderr.write("   旧链接已清除" + chr(10))

	# ── 1. 加载所有知识元（只取 H1 标题 + 正文） ──
	units = []
	for f in sorted(units_dir.glob("*.md")):
		try:
			content = f.read_text(encoding="utf-8", errors="ignore")
			if not content.startswith("---"):
				continue
			parts = content.split("---", 2)
			if len(parts) < 3:
				continue
			fm = parts[1]
			body = parts[2]
			title = ""
			m = re.search(r'^#\s*(.+)', body, re.M)
			if m:
				title = m.group(1)
			if not title:
				title = f.stem
			body_clean = re.sub(r'##\s*关\s*联.*', '', body, flags=re.DOTALL)
			body_clean = re.sub(r'[#*\[\]!|>\-=\n]', ' ', body_clean)[:2000]

			# 提取 summary（连接到正文前参与相似度计算）
			_summary = ""
			_sm = re.search(r"^summary:\s*(.+)", fm, re.MULTILINE)
			if _sm:
				_summary = _sm.group(1).strip().strip('"').strip("'")

			# 提取 tags（兼容 [...] 和 "..." 两种格式）
			_tags = []
			_tm = re.search(r'^tags:\s*\[(.+?)\]', fm, re.MULTILINE)
			if not _tm:
				_tm = re.search(r'^tags:\s*"([^"]*)"', fm, re.MULTILINE)
			if _tm:
				_tags = [t.strip().strip('"').strip("'") for t in _tm.group(1).split(",")]

			# 提取 source（知识元来源文件）
			_source = ""
			_sm2 = re.search(r'^source:\s*"([^"]*)"', fm, re.MULTILINE)
			if _sm2:
				_source = _sm2.group(1).strip()
			if not _source:
				_sm2 = re.search(r"^source:\s*'([^']*)'", fm, re.MULTILINE)
				if _sm2:
					_source = _sm2.group(1).strip()
			units.append({
				"file": f, "name": f.stem, "title": title,
				"fm_text": fm, "body": body,
				"text": (_summary + " " if _summary else "") + title + " " + body_clean,
				"tags": _tags,
				"source": _source,
			})
		except Exception:
			continue
	if not units:
		return {"error": "没有找到知识元"}
	_hb_update(phase="loading", phase_name="已加载知识元", current=2, total=5,
	               detail=f"共 {len(units)} 个知识元")
	if verbose:
		_sys.stderr.write(f"   加载了 {len(units)} 个知识元" + chr(10))

	# ── 4. 加载所有 .ctx 文件
	ctx_files = []
	for subdir in ["images", "videos", "audios", "others"]:
		d = resource_base / subdir
		if not d.exists():
			continue
		for f in d.glob("*.ctx"):
			try:
				if os.name == "nt":
					os.chmod(str(f), 0o666)
				content = f.read_text(encoding="utf-8", errors="ignore")
				chunk_heading = ""
				m = re.search(r'chunk_heading:\s*"(.+)"', content)
				if m:
					chunk_heading = m.group(1)
				resource_file = ""
				m = re.search(r'resource_file:\s*"(.+)"', content)
				if m:
					resource_file = m.group(1)
				parts = content.split("---", 2)
				ctx_body = parts[2] if len(parts) >= 3 else ""
				ctx_text_str = " ".join(
					l.strip().lstrip(">").strip()
					for l in ctx_body.split("\n") if l.strip() and not l.startswith("![[")
				)

				# 跳过单身 .ctx（无对应媒体文件）
				if resource_file and not (d / resource_file).exists():
					stem = f.stem
					found = False
					for ext in ['.png', '.jpg', '.jpeg', '.gif', '.bmp', '.webp',
								 '.mp4', '.avi', '.mov', '.mp3', '.wav']:
						if (d / (stem + ext)).exists():
							found = True
							break
					if not found:
						continue
				ctx_files.append({
					"path": str(f.relative_to(Path(workspace)).as_posix()), "abspath": str(f),
					"filename": f.name,
					"chunk_heading": chunk_heading,
					"resource_file": resource_file,
					"text": chunk_heading + " " + ctx_text_str,
					"tags_str": _extract_ctx_tags(content),
					"importance": _extract_ctx_importance(content),
					"user_edited": _extract_ctx_user_edited(content),
				})
			except Exception:
				# .ctx 文件损坏/不可读 → 移入回收站
				_trash_file(f, workspace)
	_hb_update(phase="loading", phase_name="已加载资源", current=3, total=5,
	               detail=f"共 {len(ctx_files)} 个资源文件")

	if not ctx_files:
		if verbose:
			_sys.stderr.write("   (没有 .ctx 文件，跳过资源匹配)" + chr(10))
	if verbose:
		_sys.stderr.write(f"   加载了 {len(ctx_files)} 个资源" + chr(10) + chr(10))

	# ── 5. 加载所有原始文件 chunk ──
	all_chunks = []
	try:
		all_chunks = load_all_chunks_with_text(workspace)
	except Exception:
		pass
	if verbose:
		if all_chunks:
			_chunk_sources = len(set(c["source_file"] for c in all_chunks))
			_sys.stderr.write(f"   加载了 {len(all_chunks)} 个 chunk (来自 {_chunk_sources} 个原始文件)" + chr(10) + chr(10))
		else:
			_sys.stderr.write(f"   (没有 chunk 数据，跳过原始文件关联)" + chr(10) + chr(10))

# ── 预热 jieba ──
	jieba.analyse.extract_tags("系统", topK=1)

	# --- 构建标签 IDF 字典（逆频率加权，稀有标签权重大）---
	import math
	_tag_freq = {}
	for _u in units:
		for _t in (_u.get("tags", []) or []):
			_tl = _t.lower().strip()
			if _tl:
				_tag_freq[_tl] = _tag_freq.get(_tl, 0) + 1
	_total_n = len(units)
	_tag_idf = {}
	for _t, _c in _tag_freq.items():
		_tag_idf[_t] = math.log(_total_n / max(_c, 1)) if _total_n > 0 else 0.0

	# --- Main loop: per-unit match and write ---
	unit_lookup = {u["name"]: u for u in units}
	_unit_names_sorted = sorted([u["name"] for u in units], key=len, reverse=True)
	weights = _load_weights(workspace)
	_k_weights = weights
	_k_density = max(0.1, _k_weights.get("cLinksDensity", 0.5))
	_k_max_links = max(5, int(20 * _k_weights["cLinksNum"]))
	_k_min_score = max(0.05, 0.3 * (1 - _k_density))
	_ke_total_new = 0
	_ke_linked_count = 0
	w_ctx = weights["cContext"]
	w_tags = weights["cTags"]
	w_stars = weights["cStars"]
	w_edit = weights["cEdited"]
	max_res_links = max(5, int(30 * weights["cLinksNum"]))
	max_possible = 100 * w_ctx + 100 * w_tags + 10 * w_stars + 2 * w_edit
	density = max(0.1, weights.get("cLinksDensity", 0.5))
	res_min_score = max_possible * (1 - density ** 0.6)
	ctx_to_units = {}
	# 预建 TF-IDF 向量缓存（核心性能优化：每个文本只调一次 jieba）
	_hb_update(phase="loading", phase_name="预建向量缓存", current=3, total=5, detail="正在提取 TF-IDF 关键词...")
	_pre_ke_vecs = {u["name"]: _build_tfidf_vector(u["text"]) for u in units}
	_pre_ctx_vecs = {c["path"]: _build_tfidf_vector(c["text"]) for c in ctx_files}
	_pre_chunk_vecs = {}
	if all_chunks:
		for _ci, _ch in enumerate(all_chunks):
			_pre_chunk_vecs[_ci] = _build_tfidf_vector(_ch.get("text", ""))
	units_updated = 0
	total_matches = 0
	_chunk_match_result = {"units_matched": 0, "total_file_refs": 0}
	n1 = n2 = n3 = n4 = n5p = 0
	for ui, u in enumerate(units, 1):
		_check_pause()
		# 心跳：每 5 个知识元输出一次进度
		if ui % 5 == 0 or ui == 1 or ui == len(units):
			_hb_update(phase="matching", phase_name="知识元匹配中",
			           current=ui, total=len(units),
			           detail=("正在处理第 %d/%d 个知识元: %s" % (ui, len(units), u["name"])))
		if verbose:
			_sys.stderr.write(G + chr(10) + "=" * 75 + R + chr(10))
			_sys.stderr.write(G + "> 知识元 [" + str(ui) + "/" + str(len(units)) + "]: " + u["name"] + R + chr(10))
			_sys.stderr.write(G + "=" * 75 + R + chr(10))
			_sys.stderr.flush()

		# ── A0. 硬关联检测：本知识元正文中出现的其他知识元名称 ──
		_hard_links = set()
		_hsearch = u.get("fm_text", "") + " " + u.get("body", "")
		_hsearch = re.sub(r'##\s*关\s*联.*?(?=##|\Z)', '', _hsearch, flags=re.DOTALL)
		_hsearch = re.sub(r'!\[\[[^\]]+\]\]', '', _hsearch)
		_hsearch = re.sub(r'\[\[([^\]]+)\]\]', '', _hsearch)
		_hsearch = re.sub(r'[#*>`\-=\n\r]', ' ', _hsearch)
		for _hother in _unit_names_sorted:
			if _hother == u["name"] or not _hother:
				continue
			if _hother in _hsearch:
				_hard_links.add(_hother)
				_hsearch = _hsearch.replace(_hother, '')
		if verbose:
			_sys.stderr.write(Y + "  -- 知识元名称硬关联 --" + R + chr(10))
			_sys.stderr.write(W + "o 硬关联知识元: " + str(len(_hard_links)) + "个" + R + chr(10))
			for _hl in sorted(_hard_links):
				_sys.stderr.write(W + "    -> [[" + _hl + "]]" + R + chr(10))

		# --- A. KE <-> KE matching ---
		_existing = set()
		for _m in re.finditer(r"\[\[([^\]]+?)\]\]", u["body"]):
			_ref = _m.group(1).split("|")[0].strip().lstrip("#")
			_existing.add(_ref)
		_scores_ke = []
		for _v in units:
			if u["name"] == _v["name"]: continue
			_cs = _vec_cosine(_pre_ke_vecs[u["name"]], _pre_ke_vecs[_v["name"]])
			_u_tags = set(_t.lower() for _t in u.get("tags", []))
			_v_tags = set(_t.lower() for _t in _v.get("tags", []))
			_common = _u_tags & _v_tags
			_all_tags = _u_tags | _v_tags
			_numer = sum(_tag_idf.get(_t, 0.0) for _t in _common)
			_denom = sum(_tag_idf.get(_t, 0.0) for _t in _all_tags)
			_ts = _numer / max(_denom, 0.001)

			# 名字相似度：bigram 杰卡德
			_ns = _title_bigram_sim(u["title"], _v["title"])

			# 名字引用：u的名称是否出现在_v的正文中
			_nr = 1.0 if u["title"] and u["title"] in _v["text"] else 0.0

			# 标题命中加分：人名/术语/概念在另一个知识元正文中被提及，直加10分
			_name_in_body = 0.10 if u["title"] and len(u["title"]) >= 2 and u["title"] in _v["text"] else 0.0
			_combined = _cs * 0.40 + _ts * 0.35 + _ns * 0.10 + _nr * 0.15 + _name_in_body
			_scores_ke.append((_v["name"], _combined, _cs, _ts, _ns, _nr, _name_in_body))
		_scores_ke.sort(key=lambda x: -x[1])
		_new_links = []
		# ── 硬关联排在最前面 ──
		for _ha_name in sorted(_hard_links):
			if _ha_name not in _new_links and _ha_name not in _existing:
				_new_links.append(_ha_name)
		# ── TF-IDF 语义匹配排在后面 ──
		for item in _scores_ke:
			_name, _sc = item[0], item[1]
			if _sc < _k_min_score: break
			if _name not in _new_links and _name not in _existing:
				_new_links.append(_name)
			if len(_new_links) >= _k_max_links: break

		# No orphan rule: every KE must have at least 1 outgoing link
		if not _new_links and not _existing and _scores_ke:
			_new_links.append(_scores_ke[0][0])

		_ke_total_new += len(_new_links)
		if _new_links: _ke_linked_count += 1
		if verbose:
			_sys.stderr.write(Y + "  -- 知识元链接：得分 --" + R + chr(10))
			_dn = min(8, len(_scores_ke))
			for _ri in range(_dn):
				_name, _sc, _cs, _ts, _ns, _nr, _nb = _scores_ke[_ri]
				_sys.stderr.write("  [" + str(_ri+1) + "] " + _shorten(_name, 28) + ": " + str(round(_sc*100)) + " (内容" + str(round(_cs*100)) + "x0.40+标签" + str(round(_ts*100)) + "x0.35+名称" + str(round(_ns*100)) + "x0.10+引用" + str(round(_nr*100)) + "x0.15+命中" + str(round(_nb*100)) + ")" + R + chr(10))
			if len(_scores_ke) > _dn:
				_sys.stderr.write(Y + "  ..." + R + chr(10))
				_n2, _s2 = _scores_ke[-1][0], _scores_ke[-1][1]
				_sys.stderr.write("  [" + str(len(_scores_ke)) + "] " + _shorten(_n2, 28) + ": " + str(round(_s2*100)) + R + chr(10))
			if _new_links:
				_sys.stderr.write(W + "o 关联知识元: " + str(len(_new_links)) + "个" + R + chr(10))
				for _nl in _new_links:
					_sys.stderr.write(W + "    -> [[" + _nl + "]]" + R + chr(10))
			else:
				_sys.stderr.write("o 无新增关联知识元" + chr(10))
			_sys.stderr.flush()

		# --- B. KE <-> Resource matching ---
		_all_scores = []
		for _ctx in ctx_files:
			_ctx_score = _vec_cosine(_pre_ctx_vecs[_ctx["path"]], _pre_ke_vecs[u["name"]]) * 100
			_tag_score = _tags_similarity(_ctx.get("tags_str", ""), u["text"]) * 100
			_imp = _ctx.get("importance", 3)
			_star_score = min(_imp, 5) * 2
			_edit_score = 2 if _ctx.get("user_edited", 0) else 0
			_total = _ctx_score * w_ctx + _tag_score * w_tags + _star_score * w_stars + _edit_score * w_edit
			_all_scores.append((_ctx, round(_total, 1), _ctx_score, _tag_score, _star_score, _edit_score))
		_all_sorted = sorted(_all_scores, key=lambda x: -x[1])
		_best_matches = [(_c, _s) for _c, _s, _, _, _, _ in _all_sorted if _s >= res_min_score][:max_res_links]
		if verbose:
			_sys.stderr.write(Y + "  -- 资源链接：得分 --" + R + chr(10))
			_dc = max_res_links + 2
			for _i, _item in enumerate(_all_sorted[:_dc]):
				_c, _tot, _cs, _ts, _ss, _es = _item
				_sys.stderr.write("  [" + str(_i+1) + "] " + _shorten(_c["filename"], 25) + ": " + str(round(_tot)) + " (内容" + str(int(_cs)) + "x" + str(w_ctx) + "+标签" + str(int(_ts)) + "x" + str(w_tags) + "+重要" + str(_ss) + "x" + str(w_stars) + "+编辑" + str(_es) + "x" + str(w_edit) + ")" + R + chr(10))
			if len(_all_sorted) > _dc:
				_sys.stderr.write(Y + "  ..." + R + chr(10))
				_c, _tot = _all_sorted[-1][0], _all_sorted[-1][1]
				_sys.stderr.write("  [" + str(len(_all_sorted)) + "] " + _shorten(_c["filename"], 25) + ": " + str(round(_tot)) + R + chr(10))
			_names = [(_c["resource_file"] or _c["filename"], _s) for _c, _s in _best_matches] if _best_matches else []
		_sys.stderr.write(W + "o 关联资源: " + str(len(_names)) + "个" + R + chr(10))
		if _names:
			for _n, _s in _names:
				_sys.stderr.write(W + "    -> " + _n + R + chr(10))
			_sys.stderr.flush()

		# --- C. 知识元 ? 原始文件 chunk 匹配 ---
		_chunk_result = {"matched": [], "all_sorted": [], "w_ctx": 0.5, "w_tags": 0.5, "w_title": 0.3, "threshold": 0}
		if all_chunks:
			_chunk_result = match_unit_to_chunks(u, all_chunks, weights=weights, max_files=8,
				prebuilt_unit_vec=_pre_ke_vecs[u["name"]],
				prebuilt_chunk_vecs=_pre_chunk_vecs)
		_matched_files = _chunk_result.get("matched", [])
		_all_chunk_candidates = _chunk_result.get("all_sorted", [])
		_cw_ctx = _chunk_result.get("w_ctx", 0.5)
		_cw_tags = _chunk_result.get("w_tags", 0.5)
		_cw_title = _chunk_result.get("w_title", 0.3)
		if verbose and _all_chunk_candidates:
			_sys.stderr.write(Y + "  -- 原始文件链接：得分 --" + R + chr(10))
			_dc = min(len(_all_chunk_candidates), 10)
			for _i in range(_dc):
				_mf = _all_chunk_candidates[_i]
				_file_name = _mf["file"].split("/")[-1].split("\\")[-1]
				_pos_preview = _mf.get("positions", [])[:3]
				_pos_str = " → " + "、".join(_pos_preview) if _pos_preview else ""
				_cs = int(_mf.get("cs", 0)); _ts = int(_mf.get("ts", 0)); _tts = int(_mf.get("tts", 0))
				_detail = " (内容" + str(_cs) + "x" + str(_cw_ctx) + "+标签" + str(_ts) + "x" + str(_cw_tags) + "+标题" + str(_tts) + "x" + str(_cw_title) + ")"
				_sys.stderr.write("  [" + str(_i+1) + "] " + _shorten(_file_name, 25) + _pos_str + ": " + str(int(_mf["score"])) + _detail + R + chr(10))
			if len(_all_chunk_candidates) > _dc:
				_sys.stderr.write(Y + "  ..." + R + chr(10))
				_last = _all_chunk_candidates[-1]
				_last_name = _last["file"].split("/")[-1].split("\\")[-1]
				_sys.stderr.write("  [" + str(len(_all_chunk_candidates)) + "] " + _shorten(_last_name, 25) + ": " + str(int(_last["score"])) + R + chr(10))
			if _matched_files:
				_line_parts = []
				for _mf in _matched_files:
					_file_name = _mf["file"].split("/")[-1].split("\\")[-1]
					_pos_preview = _mf.get("positions", [])[:3]
					_pos_str = " → " + "、".join(_pos_preview) if _pos_preview else ""
					_line_parts.append(_shorten(_file_name, 20) + _pos_str)
				_sys.stderr.write(W + "o 关联原始文件: " + str(len(_matched_files)) + "个" + R + chr(10))
				for _lp in _line_parts:
					_sys.stderr.write(W + "    -> " + _lp + R + chr(10))
			else:
				_sys.stderr.write(W + "o 无关联原始文件" + R + chr(10))
			_sys.stderr.flush()

		# --- D. Accumulate ctx reverse map ---
		for _ctx, _score in _best_matches:
			_ap = _ctx["abspath"]
			if _ap not in ctx_to_units:
				ctx_to_units[_ap] = []
			ctx_to_units[_ap].append(u["name"])

		# ── 写入 related_files（知识元 ? 原始文件关联）──
		if _matched_files:
			write_related_files_to_unit(u, _matched_files, dry_run=dry_run, source_file=u.get("source", ""))

		# --- E. Build and write the KE file ---
		_res_entries = []
		_media_files = []
		for _ctx, _score in _best_matches:
			_res_entries.append("  - type: image\n    ctx: \"" + _ctx["path"] + "\"")
			_rf = _ctx.get("resource_file", "")
			if _rf and not re.search(r"!\[" + re.escape(_rf) + r"\]", u["body"]):
				_media_files.append(_rf)
		_this_n = len(_best_matches)
		total_matches += _this_n
		if _this_n == 1: n1 += 1
		elif _this_n == 2: n2 += 1
		elif _this_n == 3: n3 += 1
		elif _this_n == 4: n4 += 1
		elif _this_n >= 5: n5p += 1

		# 有资源/知识元链接/原始文件关联 任一都要写入
		if not _res_entries and not _new_links and not _matched_files: continue
		_new_fm = u["fm_text"]
		_new_fm = re.sub(r"\nresources:\n(\s+.*\n?)*", "", _new_fm)
		if _res_entries:
			_fm_lines = _new_fm.strip().split("\n")
			_fm_lines.append("resources:\n" + "\n".join(_res_entries))
			_new_fm = "\n".join(_fm_lines)
		_new_body = u["body"]
		_insert_at = len(_new_body)
		for _marker in ["## 标签", "## 知识元标签"]:
			_pos = _new_body.find(_marker)
			if _pos >= 0:
				_insert_at = _pos
				break
		_insert_blocks = []
		if _new_links:
			_link_lines = "\n".join("  - [[" + n + "]]" for n in _new_links)
			_insert_blocks.append("## 关联知识元\n" + _link_lines)

		# ── 关联原始文件（在关联知识元之后、关联资源之前）──
		_related_section = build_related_files_section(_matched_files, source_file=u.get("source", ""))
		if _related_section:
			_insert_blocks.append(_related_section)
		if _media_files:
			_media_lines = []
			for _rf in _media_files:
				_ext = _rf.split(".")[-1].lower() if "." in _rf else ""
				if _ext in {"png","jpg","jpeg","gif","bmp","webp","svg"}:
					_media_lines.append("![[%s]]\n> 图" % _rf)
				elif _ext in {"mp4","avi","mov","webm","mkv"}:
					_media_lines.append("![[%s]]\n> 视频" % _rf)
				elif _ext in {"mp3","wav","aac","ogg","flac"}:
					_media_lines.append("![[%s]]\n> 音频" % _rf)
				else:
					_media_lines.append("![[%s]]" % _rf)
			_insert_blocks.append("## 关联资源\n" + "\n".join(_media_lines))
		if _insert_blocks:
			_prefix = _new_body[:_insert_at].rstrip()
			_suffix = _new_body[_insert_at:]
			_new_body = _prefix + "\n\n" + "\n\n".join(_insert_blocks) + "\n" + _suffix
		_new_fm = re.sub("\n{2,}", "\n", _new_fm)
		_new_content = "---\n" + _new_fm.strip() + "\n---" + _new_body
		if not dry_run:
			_saved = _safe_write_text(u["file"], _new_content)
			if _saved:
				units_updated += 1
	n0 = len(units) - (n1 + n2 + n3 + n4 + n5p)
	parts = [
		"  " + str(n0) + " 个知识元链接了 0 个资源",
		"  " + str(n1) + " 个知识元链接了 1 个资源",
		"  " + str(n2) + " 个知识元链接了 2 个资源",
		"  " + str(n3) + " 个知识元链接了 3 个资源",
		"  " + str(n4) + " 个知识元链接了 4 个资源",
		"  " + str(n5p) + " 个知识元链接了 5 个或更多资源",
	]
	_hb_update(phase="ctx_write", phase_name="写入资源关联", current=4, total=5,
	               detail=f"正在写入 {len(ctx_to_units)} 个 .ctx 的资源关联")
	ctx_updated = 0
	for ctx_path, unit_names in ctx_to_units.items():
		try:
			content = Path(ctx_path).read_text(encoding="utf-8", errors="ignore")
			existing = {m for m in re.findall(r'\[\[(.+?)\]\]', content.split("---", 2)[1] if "---" in content else content)
						if not re.search(r'\.(png|jpg|jpeg|gif|bmp|webp|svg|mp4|mp3|avi|mov|wav)$', m, re.I)}
			new_names = {n for n in unit_names} - existing
			if not new_names:
				continue
			all_names = sorted(existing | new_names)
			bt = "\n".join(f'  - [[{n}]]' for n in all_names)
			ctx_parts = content.split("---", 2)
			if len(ctx_parts) >= 3:
				fm = ctx_parts[1]; body = ctx_parts[2]
				fm = re.sub(r'\nbelongs_to:\n(\s+-.*\n?)*', '', fm)
				fm = re.sub(r'\nbelongs_to:\s*\[\]', '', fm)
				fm_lines = fm.strip().split("\n")
				fm_lines.append("belongs_to:")
				fm_lines.append(bt)
				new_content = "---\n" + "\n".join(fm_lines).strip() + "\n---" + body
				if not dry_run:
					_safe_write_text(ctx_path, new_content)
				ctx_updated += 1
		except Exception:
			continue
	if verbose:
		_sys.stderr.write(chr(10))
		_sys.stderr.write(G + "=" * 55 + R + chr(10))
		_sys.stderr.write(G + "  AHKB 知识链构建引擎 - 执行完毕" + R + chr(10))
		_sys.stderr.write(G + "=" * 55 + R + chr(10))
		_sys.stderr.write(G + "  目前知识库包含知识元: " + str(len(units)) + " 个" + R + chr(10))
		_sys.stderr.write(G + "  目前知识库包含资源: " + str(len(ctx_files)) + " 个" + R + chr(10))
		_sys.stderr.write(G + "  本次知识元间链接匹配: " + str(_ke_total_new) + " 个" + R + chr(10))
		if all_chunks:
			_sys.stderr.write(G + "  本次知识元关联原始文件: " + str(_chunk_match_result["units_matched"]) + " 个知识元, " + str(_chunk_match_result["total_file_refs"]) + " 个文件引用" + R + chr(10))
		_sys.stderr.write(G + "  本次链接资源: " + str(total_matches) + " 个" + R + chr(10))
		if parts:
			_sys.stderr.write(G + (chr(10) + "").join(parts) + R + chr(10))
		_sys.stderr.write(G + "  本次更新: " + str(units_updated) + " 个知识元, " + str(ctx_updated) + " 个 .ctx（资源匹配文件）" + R + chr(10))
		_sys.stderr.write(G + "  本次清理: " + str(cleaned_single_ctx) + " 个单身 .ctx文件" + R + chr(10))
		_sys.stderr.write(G + "  本次格式整理/修复: " + str(dedup_result['fixed_count']) + " 个知识元" + R + chr(10))
		_sys.stderr.write(G + "  本次标签去重: " + str(dedup_result['tag_fm'] + dedup_result['tag_body'] + dedup_result['res_dedup']) + " 个知识元" + R + chr(10))
		if no_ctx_resources:
			_sys.stderr.write(RD + "\n  【注意】以下资源缺少资源匹配文件(.ctx)。系统已为您自动补全，需要您打开各个相关.ctx文件，补充上下文信息:" + R + chr(10))
			for r in no_ctx_resources:
				_sys.stderr.write(RD + "    - " + r.name + R + chr(10))

	# ── 汇总 chunk 匹配统计 ──
	_chunk_match_result = {"units_matched": 0, "total_file_refs": 0}
	if all_chunks:
		_all_matches = []  # collected during the loop
		# 简单统计：重新扫描知识元中的 related_files
		for _uf in units_dir.glob("*.md"):
			try:
				_uc = _uf.read_text(encoding="utf-8", errors="ignore")
				if "related_files:" in _uc:
					_chunk_match_result["units_matched"] += 1
					# Count file references
					_fc = _uc.count("\n  - file:")
					_chunk_match_result["total_file_refs"] += _fc
			except Exception:
				pass
	_hb_stop.set()
	_hb_thread.join(timeout=5)
	# 清理 PID 文件（提前清理，避免关闭窗口时 runtime 输出 [safe-delete]）
	_cleanup_detached_pid()
	return {
		"ok": True,
		"units_updated": units_updated,
		"ctx_updated": ctx_updated,
		"matches_found": total_matches,
		"chunk_files_matched": _chunk_match_result.get("units_matched", 0),
		"chunk_file_refs": _chunk_match_result.get("total_file_refs", 0),
		"units_count": len(units),
		"ctx_count": len(ctx_files),
		"ke_total_new": _ke_total_new,
		"ke_linked": _ke_linked_count,
		"dry_run": dry_run,
	}
if __name__ == "__main__":
	import sys, datetime, platform, subprocess

	# Windows 终端 UTF-8 支持
	if platform.system() == "Windows":
		try:
			import ctypes
			kernel32 = ctypes.windll.kernel32
			kernel32.SetConsoleMode(kernel32.GetStdHandle(-11), 7)
		except Exception:
			pass

	# 弹窗模式检测
	_IS_POPUP_CHILD = "--popup-child" in sys.argv
	# detached-child 模式检测（解决大模型超时截断问题）
	_IS_DETACHED_CHILD = "--detached-child" in sys.argv
	workspace = None
	if "--workspace" in sys.argv:
		idx = sys.argv.index("--workspace")
		if idx + 1 < len(sys.argv):
			workspace = Path(sys.argv[idx + 1])
	if workspace:

		# --workspace 显式指定
		if not workspace.exists():
			print("\n?? 错误：工作空间不存在: " + str(workspace) + "\n")
			sys.exit(1)
		workspace = workspace.resolve()
	else:

		# 自动检测：从 cwd 向上找含 知识元/ 的目录
		_cwd = Path.cwd().resolve()
		for _parent in [_cwd] + list(_cwd.parents):
			if (_parent / "知识元").exists():
				workspace = _parent
				break
		if not workspace:

			# 未找到时回退到当前目录
			workspace = _cwd

	# ?? 禁止将 skill 目录作为工作空间
	_skill_dir = Path(__file__).resolve().parent.parent
	_ws_resolved = workspace.resolve()
	_skill_resolved = _skill_dir.resolve()
	if _ws_resolved == _skill_resolved or _skill_resolved in _ws_resolved.parents:
		print("\n?? 错误：不允许将 skill 目录作为工作空间！")
		print(f"  检测到工作空间路径: {workspace}")
		print(f"  Skill 目录路径: {_skill_dir}")
		print("\n  请将工作空间设置为您的 知识库 Vault 目录（如 D:\\My Documents\\AHKB-CPS），")
		print("  而不是 skill 安装目录（{_skill_dir}）。\n")
		sys.exit(1)
	dry_run = "--dry-run" in sys.argv

	# ─── detached-child 模式：PID 生命周期管理 ───
	if _IS_DETACHED_CHILD:
		_init_detached_files(workspace)
		# PID 冲突检查：如果旧进程还活着，拒绝启动
		if _PID_FILE.exists():
			try:
				old_data = json.loads(_PID_FILE.read_text(encoding="utf-8"))
				old_pid = old_data.get("pid", 0)
				if _is_pid_alive(old_pid):
					print("\n🔴 错误：知识链构建任务已在运行中（PID: %d）" % old_pid)
					print("   请等待当前任务完成，或手动终止该进程后重试。\n")
					sys.exit(1)
				else:
					# 旧 PID 已死，移入回收站
					_trash_file(_PID_FILE, _CROSSLINK_WS)
			except Exception:
				# 读取失败，移入回收站
				_trash_file(_PID_FILE, _CROSSLINK_WS)
	# 清理可能残留的旧进度/结果文件（移入回收站）
	_trash_file(_PROGRESS_FILE, workspace) if _PROGRESS_FILE and _PROGRESS_FILE.exists() else None
	_trash_file(_RESULT_FILE, workspace) if _RESULT_FILE and _RESULT_FILE.exists() else None
	# _CROSSLINK_WS 已在 _init_detached_files 中设置为 workspace
	# 立即写入初始进度，确保 LLM 首次轮询就能读到有效 JSON
	if _PROGRESS_FILE:
		try:
			from datetime import datetime as _dt
			_hb_init = json.dumps({
				"heartbeat": "alive",
				"status": "running",
				"phase": "init",
				"phase_name": "启动中",
				"done": 0, "total": 0, "pct": 0,
				"elapsed_seconds": 0,
				"last_update": _dt.now().strftime("%Y-%m-%d %H:%M:%S"),
			}, ensure_ascii=False)
			_PROGRESS_FILE.write_text(_hb_init, encoding="utf-8")
		except Exception:
			pass
		# 写入新 PID
		_write_detached_pid()
		# 自我授权：detached 模式下跨联引擎直接运行，无需 ahkb.py GUI 授权
		_GUI_AUTHORIZED = True

	# 获取 result_file 路径（如果有）
	result_file = None
	if "--result-file" in sys.argv:
		ri = sys.argv.index("--result-file")
		if ri + 1 < len(sys.argv):
			result_file = Path(sys.argv[ri + 1])

	# 弹窗逻辑：总是打开 tkinter GUI 窗口（不允许后台隐藏运行）
	if not _IS_POPUP_CHILD:
		if not result_file:
			result_dir = workspace / "临时工作文件"
			result_dir.mkdir(parents=True, exist_ok=True)
			result_file = result_dir / "_crosslink_result.json"
		if result_file.exists():
			_trash_file(result_file, workspace)

		# 启动 tkinter GUI 窗口
		try:
			import tkinter as tk
			from tkinter import scrolledtext, messagebox
			import threading
			root = tk.Tk()
			root.title("AHKB 知识链构建引擎")
			root.geometry("900x650")
			root.lift()
			root.focus_force()
			root.after(100, lambda: [root.lift(), root.focus_force()])

			# ── 全局配色（统一变量，随页面自动调整） ──
			BG_COLOR = '#1e1e1e'      # 深色背景
			FG_COLOR = '#d4d4d4'      # 浅色前景文字
			root.configure(bg=BG_COLOR)
			root.lift()
			root.attributes('-topmost', True)
			root.after(100, lambda: root.attributes('-topmost', False))

			# 文本显示区
			text_area = scrolledtext.ScrolledText(
				root, wrap=tk.WORD, font=("Consolas", 10),
				bg=BG_COLOR, fg=FG_COLOR, insertbackground='white',
				relief=tk.FLAT, borderwidth=0
			)
			text_area.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)

			# 状态栏
			status_var = tk.StringVar()
			status_var.set("正在处理...")
			status_bar = tk.Label(root, textvariable=status_var, bd=1, relief=tk.SUNKEN, anchor=tk.W, bg=BG_COLOR, fg='#e8e8e8')
			status_bar.pack(fill=tk.X)

			# 重定向 stderr 到文本框（支持 ANSI 彩色）
						# 重定向 stderr 到文本框（支持 ANSI 彩色）

			class TkRedirect:
				"""将 stdout/stderr 重定向到 tkinter Text 组件，解析 ANSI 颜色并着色显示"""
				COLOR_MAP = {
					'32': 'ansi_green',       # 绿色
					'94': 'ansi_bright_blue', # 亮蓝
					'93': 'ansi_yellow',      # 黄色
					'96': 'ansi_bright_cyan', # 亮青
					'91': 'ansi_bright_red',  # 亮红
					'0': '',                  # 重置
				}

				def __init__(self, text_widget, status_var):
					self.text_widget = text_widget
					self.status_var = status_var
					self.buf_pairs = []  # [(text, tag), ...] 每段文本关联其颜色
					self.current_tag = ""
					text_widget.tag_config('ansi_green', foreground='#4EC9B0')
					text_widget.tag_config('ansi_bright_blue', foreground='#569CD6')
					text_widget.tag_config('ansi_yellow', foreground='#DCDCAA')
					text_widget.tag_config('ansi_bright_cyan', foreground='#4FC1FF')
					text_widget.tag_config('ansi_bright_red', foreground='#F44747')

				def _insert_line(self, line_text):
					"""用缓冲段中最后一个非空 tag 插入一行"""
					tag = ''
					for _, t in reversed(self.buf_pairs):
						if t:
							tag = t
							break
					if tag:
						self.text_widget.insert(tk.END, line_text + chr(10), tag)
					else:
						self.text_widget.insert(tk.END, line_text + chr(10))
					self.text_widget.see(tk.END)

				def write(self, msg):
					parts = re.split(r'(\x1b\[\d+(?:;\d+)*m)', msg)
					for part in parts:
						if not part:
							continue
						ansi_match = re.match(r'\x1b\[(\d+(?:;\d+)*)m', part)
						if ansi_match:
							code = ansi_match.group(1)
							if code == '0':
								self.current_tag = ''
							elif code in self.COLOR_MAP:
								self.current_tag = self.COLOR_MAP[code]
						else:
							while chr(10) in part:
								nl_idx = part.index(chr(10))
								chunk = part[:nl_idx]
								if chunk:
									self.buf_pairs.append((chunk, self.current_tag))
								full = ''.join(t for t, _ in self.buf_pairs)
								self._insert_line(full)
								self.buf_pairs = []
								part = part[nl_idx + 1:]
							if part:
								self.buf_pairs.append((part, self.current_tag))
					self.text_widget.update_idletasks()

				def flush(self):
					if self.buf_pairs:
						full = ''.join(t for t, _ in self.buf_pairs)
						self._insert_line(full)
						self.buf_pairs = []
						self.text_widget.see(tk.END)
						self.text_widget.update_idletasks()

			# 保存原始 stderr/stdout（用于 messagebox 弹出）
			_orig_stderr = sys.__stderr__
			_orig_stdout = sys.__stdout__
			_redirect_ui = TkRedirect(text_area, status_var)
			sys.stderr = _redirect_ui
			sys.stdout = _redirect_ui

			# 关闭确认状态
			_processing_done = [False]

			def _on_closing():
				"""关闭窗口时的确认提示。
				在 detached 模式下，用户确认关闭后写入 cancelled 结果文件，
				通知 LLM 不再重试。"""
				# 恢复原始 stderr/stdout，否则 messagebox 可能无法正常弹出
				sys.stderr = _orig_stderr
				sys.stdout = _orig_stdout
				if not _processing_done[0]:
					ret = messagebox.askokcancel(
						"确认关闭",
						"程序正在执行关联，强制关闭将导致知识库不完整、数据不一致。\n\n确定要关闭吗？",
						default="cancel",
						icon="warning"
					)
					if not ret:
						# 用户取消 → 恢复重定向，保持窗口
						sys.stderr = _redirect_ui
						sys.stdout = _redirect_ui
						return
					# 用户确认关闭：detached 模式下写入 cancelled 结果
					if _IS_DETACHED_CHILD:
						_write_detached_result("cancelled",
							reason="用户手动关闭窗口",
							elapsed_seconds=int(time.time() - _HB.get("start_time", time.time())))
						_cleanup_detached_pid()
					os._exit(1)
				else:
					if _IS_DETACHED_CHILD:
						_cleanup_detached_pid()
					root.destroy()
					sys.exit(0)

			# 拦截窗口 X 按钮
			root.protocol("WM_DELETE_WINDOW", _on_closing)

			# ? 拦截 root.destroy() 作为兜底（无论何种方式触发都生效）
			_orig_root_destroy = root.destroy

			def _wrapped_destroy():
				if not _processing_done[0]:
					_on_closing()
				else:
					_orig_root_destroy()
			root.destroy = _wrapped_destroy
			btn_frame = tk.Frame(root, bg=BG_COLOR)
			btn_frame.pack(fill=tk.X, padx=5, pady=(0,5))
			btn_exit = tk.Button(btn_frame, text="完成退出", state=tk.DISABLED,
								 font=("Microsoft YaHei", 9), bg='#0e639c', fg='white',
								 activebackground='#1177bb', relief=tk.FLAT, padx=15,
								 command=_on_closing)
			btn_exit.pack(side=tk.RIGHT)
			btn_pause = tk.Button(btn_frame, text="⏸ 暂停",
								 font=("Microsoft YaHei", 9), bg='#dcdcaa', fg='#1e1e1e',
								 activebackground='#e5e07a', relief=tk.FLAT, padx=15,
								 command=lambda: _toggle_pause(btn_pause))
			btn_pause.pack(side=tk.RIGHT, padx=(0, 5))
			tk.Label(btn_frame, text='本引擎在本地运行，不消耗 Tokens，完成时会"滴滴滴..."提醒你，然后自动或等你手动关闭',
					 font=("Microsoft YaHei", 8), bg=BG_COLOR, fg='#dcdcaa',
					 anchor='w').pack(side=tk.LEFT, padx=(5, 0), pady=3)

			def _toggle_pause(button):
				"""切换暂停/继续状态。"""
				if _PAUSE_FLAG[0]:
					_PAUSE_FLAG[0] = False
					button.config(text="⏸ 暂停", bg='#dcdcaa')
					status_var.set("继续处理...")
				else:
					_PAUSE_FLAG[0] = True
					button.config(text="▶ 继续", bg='#4ec9b0')
					status_var.set("已暂停")

			def run_task():
				try:
					result = cross_link(workspace, verbose=True, dry_run=dry_run)
					_processing_done[0] = True
					if result_file:
						result_file.write_text(json.dumps(result, ensure_ascii=False), encoding="utf-8")
					# detached 模式：写入结果文件供 LLM 读取
					if _IS_DETACHED_CHILD:
						_write_detached_result("complete",
							units_updated=result.get("units_updated", 0),
							ctx_updated=result.get("ctx_updated", 0),
							matches_found=result.get("matches_found", 0),
							units_count=result.get("units_count", 0),
							elapsed_seconds=int(time.time() - _HB.get("start_time", time.time())))
					text_area.insert(tk.END, chr(10))
					btn_exit.config(state=tk.NORMAL, text="关闭窗口")
					_PAUSE_FLAG[0] = False
					btn_pause.config(state=tk.DISABLED)
					status_var.set("处理完成")
					# 蜂鸣提示：三组，每组三声，共九声
					try:
						import winsound
						for _group in range(3):
							for _ in range(3):
								winsound.Beep(1200, 180)
								time.sleep(0.12)
							if _group < 2:
								time.sleep(0.4)
					except Exception:
						pass
				# 10秒倒计时自动关闭
					def _countdown(sec):
						if sec > 0:
							status_var.set(f"处理完成，{sec} 秒后自动关闭...")
							root.after(1000, lambda: _countdown(sec - 1))
						else:
							_on_closing()
					root.after(0, lambda: _countdown(10))
				except Exception as e:
					_processing_done[0] = True
					text_area.insert(tk.END, f"错误: {str(e)}{chr(10)}")
					btn_exit.config(state=tk.NORMAL, text="关闭窗口")
					_PAUSE_FLAG[0] = False
					btn_pause.config(state=tk.DISABLED)
					# detached 模式：写入错误结果
					if _IS_DETACHED_CHILD:
						_write_detached_result("error",
							reason=str(e)[:200],
							elapsed_seconds=int(time.time() - _HB.get("start_time", time.time())))
				finally:
					# detached 模式：清理 PID 文件
					if _IS_DETACHED_CHILD and _processing_done[0]:
						_cleanup_detached_pid()
			threading.Thread(target=run_task, daemon=True).start()
			root.mainloop()
			sys.exit(0)
		except ImportError:

			# 没有 tkinter 时回退到直接运行
			pass
		if result_file and result_file.exists():
			try:
				print(result_file.read_text(encoding="utf-8"))
				_trash_file(result_file, workspace)
			except Exception:
				pass
		sys.exit(0)

	# ── 正式执行 ──
	start_time = datetime.datetime.now()
	result = cross_link(workspace, verbose=True, dry_run=dry_run)

	# 写入运维记录
	record_dir = workspace / "运维记录"
	record_dir.mkdir(parents=True, exist_ok=True)
	record_file = record_dir / "运维记录.md"
	elapsed = (datetime.datetime.now() - start_time).total_seconds()
	existing = []
	if record_file.exists():
		existing = record_file.read_text(encoding="utf-8").split(chr(10))
	header = "# AHKB 运维记录" + chr(10) + chr(10)
	header += "| 时间 | 动作 | 结果 | 知识元 | .ctx | 匹配 | 耗时 |" + chr(10)
	header += "|------|------|------|-------|------|------|------|" + chr(10)
	new_line = "| " + start_time.strftime("%Y-%m-%d %H:%M:%S")
	new_line += " | 知识元与资源链接"
	if result.get("error"):
		new_line += " | " + result["error"]
		new_line += " | - | - | - | -"
	else:
		new_line += " | "
		ok_symbol = chr(10004) + chr(65039)
		new_line += ok_symbol
		new_line += " | " + str(result.get("units_updated",0))
		new_line += " | " + str(result.get("ctx_updated",0))
		new_line += " | " + str(result.get("matches_found",0))
		new_line += " | " + str(int(elapsed)) + "s"
	new_line += " |"
	rows = [l for l in existing if l and not l.startswith("#") and not l.startswith("|-") and "时间" not in l]
	rows.insert(0, new_line)
	with open(record_file, "w", encoding="utf-8") as f:
		f.write(header)
		f.write(chr(10).join(rows) + chr(10))
	if result_file:
		result_file.write_text(json.dumps(result, ensure_ascii=False), encoding="utf-8")