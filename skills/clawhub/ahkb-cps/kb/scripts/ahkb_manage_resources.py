#!/usr/bin/env python3
"""
ahkb_manage_resources.py — AHKB 知识库资源管理器 v0.4.0

图形界面版本，管理图片及其他资源（不管理知识元）。
"""
import os, sys, json, re, subprocess, random
sys.stdout.reconfigure(encoding='utf-8') if hasattr(sys.stdout, 'reconfigure') else None
from pathlib import Path
from datetime import datetime
from ahkb_trash import _trash_file
from collections import defaultdict
from tkinter import *
from tkinter import ttk, messagebox
from PIL import Image, ImageTk

VAULT = None
RES_BASE = None
UNITS_DIR = None
SUB_DIRS = {}


def find_workspace():
    """自动检测工作空间（Vault）路径。"""
    cwd = Path.cwd().resolve()
    for parent in [cwd] + list(cwd.parents):
        if (parent / "知识元").exists():
            return parent
    return None


def resolve_vault(args_workspace=None):
    """确定工作空间路径：优先 --workspace，其次自动检测，最后报错退出。"""
    global VAULT, RES_BASE, UNITS_DIR, SUB_DIRS
    if args_workspace:
        ws = Path(args_workspace)
        if not ws.exists():
            print(f"错误：工作空间不存在: {args_workspace}")
            sys.exit(1)
        VAULT = ws.resolve()
    else:
        detected = find_workspace()
        if detected:
            VAULT = detected
        else:
            # 未找到时回退到当前目录（适用于全新的、未初始化的知识库）
            VAULT = Path.cwd().resolve()
    RES_BASE = VAULT / "图片及其他资源"
    UNITS_DIR = VAULT / "知识元"
    SUB_DIRS = {
        "images": RES_BASE / "images", "videos": RES_BASE / "videos",
        "audios": RES_BASE / "audios", "others": RES_BASE / "others",
    }
MEDIA_EXTS = {".png", ".jpg", ".jpeg", ".gif", ".bmp", ".webp",
              ".mp4", ".avi", ".mov", ".wmv", ".flv",
              ".mp3", ".wav", ".ogg", ".wma",
              ".pdf", ".zip", ".rar", ".7z"}
THUMB_SIZE = (140, 100)
# COLS 在 __init__ 中根据屏幕宽度动态计算



def _repair_ctx_format(ctx_path, filename):
    """修复 .ctx 文件格式：拆分合并行、独立 ---、补全 ![[filename]]"""
    try:
        with open(ctx_path, "r", encoding="utf-8") as f:
            raw = f.read()
        original = raw
        # 拆分合并字段
        lines = raw.split(chr(10))
        lines = _ensure_fields_separate(lines)
        # 确保 --- 独立成行
        new_lines = []
        for line in lines:
            stripped = line.strip()
            if stripped == "---" or stripped == "" or stripped.startswith("![["):
                new_lines.append(line)
            elif "---" in line and not line.startswith("---"):
                # 行内包含 --- 但不是行首（如 tags: [...]---）
                parts = line.split("---", 1)
                new_lines.append(parts[0].rstrip())
                new_lines.append("---" + parts[1])
            else:
                new_lines.append(line)
        # 确保 ![[filename]] 存在
        media_ref = "![[{}]]".format(filename)
        has_media = any(media_ref in l for l in new_lines)
        if not has_media:
            new_lines.append(media_ref)
        # 去重 tags:
        seen_tags = False
        deduped = []
        for line in new_lines:
            if line.strip().startswith("tags:"):
                if seen_tags:
                    continue
                seen_tags = True
            deduped.append(line)
        new_lines = deduped
        # 修复 tags: [[...]] → tags: [...]（双括号）
        new_lines = [re.sub(r'^(tags:\s*)\[\[(.+?)\]\]', r'\1[\2]', l) if l.strip().startswith('tags:') else l for l in new_lines]
        repaired = chr(10).join(new_lines)
        if repaired != original:
            with open(ctx_path, "w", encoding="utf-8") as f:
                f.write(repaired)
    except:
        pass




class ResourceEntry:
    def __init__(self, filepath, res_type):
        self.filepath = filepath
        self.filename = filepath.name
        self.res_type = res_type
        self.ext = filepath.suffix.lower()
        self.size_bytes = filepath.stat().st_size
        self.size_str = self._fmt_size()
        self.mtime = datetime.fromtimestamp(filepath.stat().st_mtime)
        self.mtime_str = self.mtime.strftime("%Y-%m-%d %H:%M")
        self.ctx_path = filepath.with_suffix(".ctx")
        self.has_ctx = self.ctx_path.exists()
        self.belongs_to = []
        self.tags = []
        self.chunk_heading = ""
        self.source = ""
        self.keywords = ""
        self.ctx_edited = False
        self.user_edited = False
        self.last_edited = ""
        self.importance = 3  # 1-5
        self.dim_pixels = 0  # 图片宽x高
        self.dim_str = "?"
        try:
            with Image.open(filepath) as im:
                self.dim_pixels = im.width * im.height
                self.dim_str = f"{im.width}x{im.height}"
        except:
            pass
        if self.has_ctx:
            self._parse_ctx()

    def _fmt_size(self):
        s = self.size_bytes
        if s < 1024: return f"{s}B"
        elif s < 1024*1024: return f"{s//1024}KB"
        else: return f"{s/(1024*1024):.1f}MB"

    def _parse_ctx(self):
        try:
            with open(self.ctx_path, "r", encoding="utf-8") as f:
                content = f.read()
            self.belongs_to = re.findall(r'- \[\[(.+?)\]\]', content)
            # 只在 --- 之间的 frontmatter 中查找 tags
            fm_part = content
            if content.startswith("---"):
                parts = content.split("---", 2)
                if len(parts) >= 3:
                    fm_part = parts[1]
            tg = re.search(r'^tags:\s*\[\[(.*?)\]\]|^tags:\s*\[(.*?)\]', fm_part, re.MULTILINE)
            if tg:
                val = tg.group(1) or tg.group(2)
                self.tags = [t.strip().strip("[]") for t in val.split(",") if t.strip()]
            ch = re.search(r'chunk_heading:\s*"(.+?)"', content)
            if ch: self.chunk_heading = ch.group(1)
            sc = re.search(r'source:\s*"(.+?)"', content)
            if sc: self.source = sc.group(1)
            self.ctx_edited = len(self.belongs_to) > 0
            self.user_edited = "user_edited: true" in content
            imp = re.search(r'^importance:\s*(\d+)', content, re.MULTILINE)
            self.importance = int(imp.group(1)) if imp else 3
            le = re.search(r'^last_edited_time:\s*(.*)', content, re.MULTILINE)
            le_val = le.group(1).strip() if le and le.group(1).strip() else ""
            # 检查是否误吞了下一行内容
            if le_val and "\n" in content:
                nxt = content.index("\n", content.index("last_edited_time")) + 1
                if le_val == content[nxt:].split("\n")[0].strip():
                    le_val = ""
            if le_val:
                self.last_edited = le_val
            else:
                # 若 last_edited_time 为空或无此字段，用 ctx 文件修改时间补上
                ctx_mtime = ""
                try:
                    ct = datetime.fromtimestamp(self.ctx_path.stat().st_mtime)
                    ctx_mtime = ct.strftime("%Y-%m-%d %H:%M:%S")
                except: pass
                self.last_edited = ctx_mtime
                # 写回 .ctx — 逐行处理确保字段完整顺序正确
                lines = _ensure_fields_separate(content.split(chr(10)))
                new_lines = []
                had_imp = "importance:" in content
                had_ue = "user_edited:" in content
                had_le = "last_edited_time:" in content
                for line in lines:
                    new_lines.append(line)
                    if line.strip().startswith("type: resource") and not had_imp:
                        new_lines.append("importance: 3")
                        had_imp = True
                    if line.strip().startswith("resource_type:") and not (had_ue and had_le):
                        if not had_ue:
                            new_lines.append("user_edited: false")
                            had_ue = True
                        if not had_le:
                            new_lines.append("last_edited_time: " + ctx_mtime)
                            had_le = True
                    if line.strip().startswith("last_edited_time:") and had_le:
                        val = line.split(":", 1)
                        if len(val) > 1 and not val[1].strip():
                            new_lines[-1] = "last_edited_time: " + ctx_mtime
                new_content = chr(10).join(new_lines)
                # 确保 ![[filename]] 存在
                media_ref = "![[{}]]".format(self.filepath.name)
                if media_ref not in new_content:
                    new_content = new_content.rstrip(chr(10)) + chr(10) + media_ref
                if new_content != content:
                    with open(self.ctx_path, "w", encoding="utf-8") as f:
                        f.write(new_content)
            kw = self.tags[:]
            if self.chunk_heading: kw.append(self.chunk_heading)
            if self.source: kw.append(Path(self.source).stem)
            self.keywords = " ".join(kw)
        except Exception:
            pass


# ─── 核心功能 ─────────────────────────────────────────
def scan_resources():
    resources = []
    for res_type, dir_path in SUB_DIRS.items():
        if not dir_path.exists(): continue
        for f in dir_path.iterdir():
            if f.suffix.lower() == ".ctx": continue
            if res_type != "others" and f.suffix.lower() not in MEDIA_EXTS: continue
            try: resources.append(ResourceEntry(f, res_type))
            except Exception: pass
    resources.sort(key=lambda r: r.mtime, reverse=True)
    return resources


def search_resources(resources, query):
    q = query.lower().strip()
    if not q: return resources
    return [r for r in resources if
            q in r.filename.lower() or q in r.keywords.lower() or
            any(q in bt.lower() for bt in r.belongs_to) or q in r.source.lower()]


def filter_resources(resources, mode):
    if mode == "unlinked": return [r for r in resources if r.has_ctx and not r.belongs_to]
    if mode == "has_ctx": return [r for r in resources if r.has_ctx]
    if mode == "no_ctx": return [r for r in resources if not r.has_ctx]
    return resources


def delete_resource(resource):
    deleted = []
    if resource.filepath.exists():
        _trash_file(resource.filepath, VAULT)
        deleted.append(resource.filename)
    if resource.ctx_path.exists():
        _trash_file(resource.ctx_path, VAULT)
        deleted.append(resource.ctx_path.name)
    _clean_knowledge_refs(resource)
    return len(deleted) > 0


def _clean_knowledge_refs(resource):
    if not UNITS_DIR.exists(): return
    for unit_file in UNITS_DIR.iterdir():
        if unit_file.suffix != ".md": continue
        try:
            with open(unit_file, "r", encoding="utf-8") as f:
                content = f.read()
            new_content = content.replace(f"![[{resource.filename}]]", "")
            new_content = re.sub(
                rf'  - type:.*\n    ctx: ".*?{re.escape(resource.filename)}.*?"\n?',
                "", new_content)
            if new_content != content:
                with open(unit_file, "w", encoding="utf-8") as f:
                    f.write(new_content)
        except: pass


# ─── 图形界面 ─────────────────────────────────────────

def _ensure_fields_separate(lines):
    """确保 frontmatter 中每个字段独立成行（使用单词边界避免误拆子串）"""
    FIELD_NAMES = ('type:', 'resource_type:', 'importance:', 'user_edited:',
                   'last_edited_time:', 'source:', 'belongs_to_chunk:',
                   'chunk_heading:', 'resource_file:', 'tags:', 'belongs_to:')
    result = []
    for line in lines:
        splits = []
        for f in FIELD_NAMES:
            # 使用 \b 单词边界避免匹配到字段名子串（如 type: 匹配到 resource_type: 内部）
            for m in re.finditer(r'\b' + re.escape(f), line):
                idx = m.start()
                if idx > 0:
                    splits.append((idx, f))
        if splits:
            splits.sort()
            last = 0
            for pos, f in splits:
                if pos > last:
                    result.append(line[last:pos].rstrip())
                    last = pos
            result.append(line[last:])
        else:
            result.append(line)
    return result


class ResourceManagerGUI:
    def __init__(self):
        self.root = Tk()
        self.root.title("AHKB 资源管理器 v0.4.0")
        self.root.geometry("1150x780")
        self.root.minsize(800, 500)
        self.root.state('zoomed')  # 启动时最大化
        self.root.lift()
        self.root.focus_force()
        self.root.after(100, lambda: [self.root.lift(), self.root.focus_force()])
        self.root.update()
        # 根据屏幕宽度计算列数和卡片宽度
        self._recalc_layout()

        self.all_resources = scan_resources()
        self.filtered = list(self.all_resources)
        self.selected = set()
        self.thumbs_cache = {}
        self.current_mode = "all"
        self.current_query = ""
        self.page = 0
        self.per_page = 30
        self.size_asc = False  # 尺寸排序方向
        self.time_asc = False  # 时间排序方向
        self.type_order = ["全部", "图片", "视频", "音频", "其他"]
        self.type_idx = 0  # 当前类型索引

        self._build_ui()
        self._refresh_display()
        self.root.bind("<Configure>", self._on_resize)

    def _build_ui(self):
        # ── 顶部 ──
        top = Frame(self.root, bg="#1a1a2e", height=40)
        top.pack(fill=X)
        Label(top, text="AHKB 资源管理器", font=("微软雅黑", 18, "bold"),
              fg="#58a6ff", bg="#1a1a2e").pack(side=LEFT, padx=12)
        self.lbl_stats = Label(top, text="", font=("微软雅黑", 12),
                               fg="#8b949e", bg="#1a1a2e")
        self.lbl_stats.pack(side=LEFT, padx=10)

        # ── 工具栏 ──
        bar = Frame(self.root, bg="#0d1117")
        bar.pack(fill=X, padx=10, pady=(6, 2))

        self.search_var = StringVar()
        Entry(bar, textvariable=self.search_var, font=("微软雅黑", 11),
              bg="#161b22", fg="#c9d1d9", insertbackground="#c9d1d9",
              relief="solid", highlightthickness=1, highlightbackground="#58a6ff",
              width=28).pack(side=LEFT, padx=(5, 4))
        Button(bar, text="搜索", command=self._on_search,
               bg="#21262d", fg="white", relief="flat", padx=10,
               font=("微软雅黑", 11)).pack(side=LEFT, padx=2)
        self.clear_btn = Button(bar, text="清除搜索", command=self._clear_search,
               bg="#21262d", fg="#484f58", relief="flat", padx=10,
               font=("微软雅黑", 11), state=DISABLED)
        self.clear_btn.pack(side=LEFT, padx=2)

        Button(bar, text="类型", command=self._cycle_type,
               bg="#21262d", fg="white", relief="flat", padx=8,
               font=("微软雅黑", 11)).pack(side=LEFT, padx=2)
        self.lbl_type = Label(bar, text="全部", font=("微软雅黑", 11),
                              fg="#f85149", bg="#0d1117")
        self.lbl_type.pack(side=LEFT, padx=(0, 6))

        self.filter_var = StringVar(value="全部")
        for f in ["本类全部", "未关联", "无 .ctx"]:
            Radiobutton(bar, text=f, variable=self.filter_var, value=f,
                       command=self._on_filter, bg="#0d1117", fg="#3fb950",
                       font=("微软雅黑", 11),
                       selectcolor="#0d1117", activebackground="#0d1117").pack(side=LEFT, padx=2)

        Radiobutton(bar, text="尺寸", variable=self.filter_var, value="尺寸",
                   command=self._on_filter, bg="#0d1117", fg="#3fb950",
                   font=("微软雅黑", 11),
                   selectcolor="#0d1117", activebackground="#0d1117").pack(side=LEFT, padx=2)
        self.lbl_size = Label(bar, text="", font=("微软雅黑", 11),
                              fg="#58a6ff", bg="#0d1117")
        self.lbl_size.pack(side=LEFT, padx=(0, 6))

        Radiobutton(bar, text="时间", variable=self.filter_var, value="时间",
                   command=self._on_filter, bg="#0d1117", fg="#3fb950",
                   font=("微软雅黑", 11),
                   selectcolor="#0d1117", activebackground="#0d1117").pack(side=LEFT, padx=2)
        self.lbl_time = Label(bar, text="", font=("微软雅黑", 11),
                              fg="#58a6ff", bg="#0d1117")
        self.lbl_time.pack(side=LEFT, padx=(0, 6))

        # 操作按钮
        for txt, cmd, color in [
            ("退出", self._exit_app, "#da3633"),
            ("删 除", self._delete_selected, "#da3633"),
            ("统计", self._show_stats, "#21262d"),
            ("刷新", self._refresh, "#21262d"),
            ("清空选择", self._clear_selection, "#21262d"),
            ("全选本页", self._select_page, "#21262d"),
        ]:
            Button(bar, text=txt, command=cmd, bg=color, fg="white",
                   relief="flat", padx=8, font=("微软雅黑", 11)).pack(side=RIGHT, padx=2)

        # ── 翻页 ──
        page_frame = Frame(self.root, bg="#0d1117")
        page_frame.pack(fill=X, padx=10, pady=(0, 4))
        self.lbl_page = Label(page_frame, text="", font=("微软雅黑", 11),
                              fg="#58a6ff", bg="#0d1117")
        self.lbl_page.pack(side=LEFT, padx=2)
        self.btn_prev = Button(page_frame, text="◀ 上一页", command=self._prev_page,
                               bg="#21262d", fg="white", relief="flat", padx=10,
                               font=("微软雅黑", 11))
        self.btn_prev.pack(side=LEFT, padx=2)
        self.btn_next = Button(page_frame, text="下一页 ▶", command=self._next_page,
                               bg="#21262d", fg="white", relief="flat", padx=10,
                               font=("微软雅黑", 11))
        self.btn_next.pack(side=LEFT, padx=2)
        self.page_slider = Scale(page_frame, from_=1, to=10, orient=HORIZONTAL,
                                 command=self._slider_page, showvalue=False,
                                 bg="#0d1117", fg="#58a6ff", troughcolor="#8b949e",
                                 activebackground="#79c0ff",
                                 highlightthickness=0, bd=0, length=160,
                                 sliderlength=16, width=12)
        self.page_slider.pack(side=LEFT, padx=6)
        self.lbl_slider_val = Label(page_frame, text="1", font=("微软雅黑", 11),
                                    fg="#58a6ff", bg="#0d1117", width=4)
        self.lbl_slider_val.pack(side=LEFT, padx=(2, 8))

        # ── 滚动网格 ──
        container = Frame(self.root, bg="#0d1117")
        container.pack(fill=BOTH, expand=True, padx=10, pady=(4, 6))

        canvas = Canvas(container, bg="#0d1117", highlightthickness=0)
        vbar = Scrollbar(container, orient=VERTICAL, command=canvas.yview)
        self.grid_frame = Frame(canvas, bg="#0d1117")

        self.grid_frame.bind("<Configure>",
            lambda e: canvas.configure(scrollregion=canvas.bbox("all")))
        canvas.create_window((0, 0), window=self.grid_frame, anchor="nw")
        canvas.configure(yscrollcommand=vbar.set)

        canvas.pack(side=LEFT, fill=BOTH, expand=True)
        vbar.pack(side=RIGHT, fill=Y)

        def _wheel(event):
            if event.widget.winfo_toplevel() == self.root:
                canvas.yview_scroll(-1 * (event.delta // 120), "units")
        self.root.bind("<MouseWheel>", _wheel, add="+")

        # ── 状态栏 ──
        status = Frame(self.root, bg="#161b22", height=22)
        status.pack(fill=X)
        self.lbl_status = Label(status, text="就绪", font=("微软雅黑", 11),
                                fg="#8b949e", bg="#161b22", anchor="w")
        self.lbl_status.pack(side=LEFT, padx=10, fill=X)

    # ── 显示 ──
    def _refresh(self):
        self.all_resources = scan_resources()
        self.search_var.set("")
        self.current_query = ""
        self.filter_var.set("本类全部")
        self.current_mode = "all"
        self.type_idx = 0
        self.lbl_type.config(text="全部")
        self.page = 0
        self.selected = set()
        self._apply_filter()



    def _clear_selection(self):
        self.selected = set()
        self._refresh_display()

    def _select_page(self):
        self.selected = set()
        start = self.page * self.per_page
        end = min(start + self.per_page, len(self.filtered))
        self.selected = set(range(start, end))
        self._refresh_display()

    def _prev_page(self):
        if self.page > 0:
            self.page -= 1
            self.selected = set()
            self._refresh_display()

    def _next_page(self):
        total = len(self.filtered)
        total_pages = max(1, (total + self.per_page - 1) // self.per_page)
        if self.page < total_pages - 1:
            self.page += 1
            self.selected = set()
            self._refresh_display()

    def _slider_page(self, val):
        p = int(float(val)) - 1
        if p != self.page:
            self.page = p
            self.selected = set()
            self._refresh_display()
        else:
            self.lbl_slider_val.config(text=str(p + 1))

    def _recalc_layout(self):
        w = self.root.winfo_width()
        if w > 100:
            avail = w - 80  # 减去边距(20) + 滚动条(20) + 余量(40)
            self.cols = max(2, avail // 185)
            self.card_w = avail // self.cols
            self.thumb_w = self.card_w - 12
            self.thumb_h = int(self.thumb_w * 0.85)

    def _on_resize(self, event):
        if event.widget == self.root:
            old_cols = self.cols
            self._recalc_layout()
            if self.cols != old_cols:
                self._refresh_display()

    def _cycle_type(self):
        self.type_idx = (self.type_idx + 1) % len(self.type_order)
        self.lbl_type.config(text=self.type_order[self.type_idx])
        self._apply_filter()

    def _on_search(self):
        self.current_query = self.search_var.get()
        if self.current_query:
            self.clear_btn.config(state=NORMAL, fg="white")
        self._apply_filter()

    def _clear_search(self):
        self.search_var.set("")
        self.current_query = ""
        self.filter_var.set("本类全部")
        self.current_mode = "all"
        self.type_idx = 0
        self.lbl_type.config(text="全部")
        self.size_asc = False
        self.time_asc = False
        self.lbl_size.config(text="")
        self.lbl_time.config(text="")
        self.clear_btn.config(state=DISABLED, fg="#484f58")
        self._apply_filter()

    def _on_filter(self):
        self.lbl_size.config(text="")
        self.lbl_time.config(text="")
        fv = self.filter_var.get()
        if fv == "尺寸":
            self.size_asc = not self.size_asc
            self.lbl_size.config(text="↑" if self.size_asc else "↓")
        elif fv == "时间":
            self.time_asc = not self.time_asc
            self.lbl_time.config(text="↑" if self.time_asc else "↓")
        self._apply_filter()

    def _apply_filter(self):
        mode_map = {"本类全部": "all", "未关联": "unlinked", "无 .ctx": "no_ctx", "尺寸": "small", "时间": "time"}
        self.current_mode = mode_map.get(self.filter_var.get(), "all")
        f = search_resources(self.all_resources, self.current_query)
        self.filtered = filter_resources(f, self.current_mode)
        # 类型筛选
        t = self.type_order[self.type_idx]
        type_map = {"图片":"images", "视频":"videos", "音频":"audios", "其他":"others"}
        if t in type_map:
            self.filtered = [r for r in self.filtered if r.res_type == type_map[t]]
        # 排序：尺寸按大小排（可切换方向），其他按时间从新到老
        ts = lambda r: r.mtime.timestamp()
        if self.current_mode == "small":
            # 先按尺寸排，再按时间从新到旧
            if self.size_asc:
                self.filtered.sort(key=lambda r: (r.dim_pixels, -ts(r)))
            else:
                self.filtered.sort(key=lambda r: (-r.dim_pixels, -ts(r)))
        elif self.current_mode == "time":
            # 按时间排，可切换方向
            self.filtered.sort(key=lambda r: r.mtime, reverse=not self.time_asc)
        else:
            self.filtered.sort(key=lambda r: r.mtime, reverse=True)
        self.page = 0
        self.selected = set()
        self._refresh_display()

    def _refresh_display(self):
        for w in self.grid_frame.winfo_children():
            w.destroy()
        self.thumbs_cache.clear()
        total = len(self.filtered)
        total_pages = max(1, (total + self.per_page - 1) // self.per_page)
        self.page = min(self.page, total_pages - 1)
        self.lbl_stats.config(text=f"共 {total} 个资源")

        # 更新翻页按钮和页码
        self.btn_prev.config(state=NORMAL if self.page > 0 else DISABLED)
        self.btn_next.config(state=NORMAL if self.page < total_pages - 1 else DISABLED)
        self.page_slider.config(to=max(1, total_pages), from_=1)
        self.page_slider.set(self.page + 1)
        self.lbl_slider_val.config(text=str(self.page + 1))
        start = self.page * self.per_page
        end = min(start + self.per_page, total)
        self.lbl_page.config(text=f"第 {self.page+1}/{total_pages} 页 显示 {start+1}-{end}")

        if total == 0:
            Label(self.grid_frame, text="没有匹配的资源",
                  font=("微软雅黑", 14), fg="#484f58", bg="#0d1117").pack(pady=80)
            self.lbl_status.config(text="无匹配")
            return

        page_items = self.filtered[start:end]
        for i, r in enumerate(page_items):
            abs_idx = start + i
            if i % self.cols == 0:
                row = Frame(self.grid_frame, bg="#0d1117")
                row.pack(fill=X, pady=2)
            self._create_card(row, r, abs_idx)

        self.lbl_status.config(text=f"已选 {len(self.selected)} 个 | 共 {total} 个")

    def _create_card(self, parent, r, idx):
        cw = self.card_w
        card = Frame(parent, bg="#161b22", bd=1, relief="solid",
                     highlightbackground="#484f58", highlightthickness=1,
                     padx=4, pady=4, width=cw, height=cw+95)
        card.pack(side=LEFT, padx=3)
        card.pack_propagate(False)

        # 顶栏：序号 + 勾选
        top = Frame(card, bg="#1a3a5c", height=20)
        top.pack(fill=X)
        Label(top, text=f"#{idx+1}", font=("微软雅黑", 12),
              fg="#c9d1d9", bg="#1a3a5c").pack(side=LEFT)

        is_sel = idx in self.selected
        cb_var = BooleanVar(value=is_sel)
        if is_sel:
            card.config(highlightbackground="#58a6ff", highlightthickness=2)
        def toggle(v=cb_var, c=card, i=idx):
            if v.get():
                self.selected.add(i)
                c.config(highlightbackground="#58a6ff", highlightthickness=2)
            else:
                self.selected.discard(i)
                c.config(highlightbackground="#4a6078", highlightthickness=1)
            self.lbl_status.config(text=f"已选 {len(self.selected)} 个")

        Checkbutton(top, variable=cb_var, bg="#1a3a5c",
                    fg="#8b949e", selectcolor="#1a3a5c",
                    activebackground="#1a3a5c",
                    command=toggle).pack(side=RIGHT)

        # 缩略图
        thumb = Frame(card, bg="#0d1117", height=self.thumb_h, width=self.thumb_w)
        thumb.pack(pady=2)
        thumb.pack_propagate(False)
        try:
            img = Image.open(r.filepath)
            img.thumbnail((self.thumb_w, self.thumb_h), Image.LANCZOS)
            tk_img = ImageTk.PhotoImage(img)
            self.thumbs_cache[r.filename] = tk_img
            Label(thumb, image=tk_img, bg="#0d1117").pack(expand=True)
        except:
            _type_cn = {"images":"图片","videos":"视频","audios":"音频","others":"其他"}.get(r.res_type, r.res_type)
            Label(thumb, text=f"{_type_cn}\n无预览", fg="#484f58",
                  bg="#0d1117", font=("微软雅黑", 11), justify=CENTER).pack(expand=True)

        # 文件名
        max_fn = self.card_w // 8
        fn = r.filename if len(r.filename) < max_fn else r.filename[:max_fn-3] + "..."
        Label(card, text=fn, font=("微软雅黑", 11), fg="#e6edf3",
              bg="#161b22", anchor="w").pack(fill=X)

        # 元信息第一行：尺寸 + 大小
        dim = "?"
        try:
            with Image.open(r.filepath) as im:
                dim = f"{im.width}x{im.height}"
        except: pass
        meta1 = Frame(card, bg="#161b22")
        meta1.pack(fill=X)
        Label(meta1, text=dim, font=("微软雅黑", 11),
              fg="#8b949e", bg="#161b22").pack(side=LEFT)
        Label(meta1, text=r.size_str, font=("微软雅黑", 11),
              fg="#8b949e", bg="#161b22").pack(side=RIGHT)

        # 元信息第二行：.ctx + 关联数 + 编辑
        ctx_c = "#3fb950" if r.has_ctx else "#f85149"
        ctx_t = "有ctx" if r.has_ctx else "无ctx"
        lk_c = "#3fb950" if r.belongs_to else "#f85149"
        lk_t = f"关联{len(r.belongs_to)}" if r.belongs_to else "未关联"
        meta2 = Frame(card, bg="#161b22")
        meta2.pack(fill=X)
        Label(meta2, text=ctx_t, font=("微软雅黑", 11),
              fg=ctx_c, bg="#161b22").pack(side=LEFT)
        Label(meta2, text=f" {lk_t}", font=("微软雅黑", 11),
              fg=lk_c, bg="#161b22").pack(side=LEFT, padx=(4,0))

        ue_c = "#d29922" if r.user_edited else "#f85149"
        ue_t = "已编辑" if r.user_edited else "未编辑"
        Label(meta2, text=ue_t, font=("微软雅黑", 11),
              fg=ue_c, bg="#161b22").pack(side=RIGHT)

        # 重要性
        stars = "★" * r.importance + "☆" * (5 - r.importance)
        imp_frame = Frame(card, bg="#161b22")
        imp_frame.pack(fill=X)
        Label(imp_frame, text="重要性", font=("微软雅黑", 11),
              fg="#c9d1d9", bg="#161b22").pack(side=LEFT)
        Label(imp_frame, text=stars, font=("微软雅黑", 11),
              fg="#d29922", bg="#161b22").pack(side=LEFT)

        # 单击缩略图和元信息区出详情
        for widget in (thumb, meta1, meta2):
            widget.bind("<Button-1>", lambda e, r=r: self._show_detail(r))
            for child in widget.winfo_children():
                try: child.bind("<Button-1>", lambda e, r=r: self._show_detail(r))
                except: pass

    # ── 操作 ──
    def _show_detail(self, r):
        w = Toplevel(self.root)
        w.title(f"资源详细信息: {r.filename}")
        win_y = int(self.root.winfo_screenheight()*0.15 + random.randint(-30,30) - 50)
        avail_h = self.root.winfo_height()
        win_h = avail_h - win_y - 20
        if win_h < 200: win_h = 200
        w.geometry(f"850x{win_h}+{int((self.root.winfo_screenwidth()-850)/2+random.randint(-40,40))}+{win_y}")
        w.configure(bg="#2d4055")
        w.transient(self.root)  # 保持在主窗口之上
        if r.has_ctx:
            _repair_ctx_format(r.ctx_path, r.filename)
        r._parse_ctx()  # 重新读取最新元数据

        # 水平布局：左图右信息
        top_h = Frame(w, bg="#364b63")
        top_h.pack(fill=X, padx=14, pady=(10, 4))

        # 左侧：图片预览
        img_frame = Frame(top_h, bg="#364b63", width=280, height=200)
        img_frame.pack(side=LEFT, padx=(0, 12))
        img_frame.pack_propagate(False)
        try:
            img = Image.open(r.filepath)
            ratio = min(270 / img.width, 190 / img.height)
            new_w = int(img.width * ratio)
            new_h = int(img.height * ratio)
            img = img.resize((new_w, new_h), Image.LANCZOS)
            tk_img = ImageTk.PhotoImage(img)
            lbl_img = Label(img_frame, image=tk_img, bg="#364b63")
            lbl_img.image = tk_img
            lbl_img.pack(expand=True)
        except Exception:
            Label(img_frame, text="[无法预览]", fg="#484f58",
                  bg="#364b63", font=("微软雅黑", 14)).pack(expand=True)

        # 右侧：详细信息（紧凑排列）
        sf = Frame(top_h, bg="#425871")
        sf.pack(side=LEFT, fill=BOTH, expand=True)
        ctx_label = "有" if r.has_ctx else "无"
        ctx_color = "#3fb950" if r.has_ctx else "#f85149"
        dims = r.dim_str

        rows_data = [
            ("文件名", r.filename, "#c9d1d9"),
            ("大小", f"{r.size_str}  ({r.size_bytes} 字节)", "#c9d1d9"),
            ("尺寸", r.dim_str, "#c9d1d9"),
            ("类型", r.res_type, "#c9d1d9"),
            (".ctx", ctx_label, ctx_color),
            ("关联", f"{len(r.belongs_to)} 个知识元" if r.belongs_to else "无", "#3fb950" if r.belongs_to else "#484f58"),
            ("来源", r.source or "--", "#8b949e"),
            ("已编辑", "是" if r.user_edited else "否", "#3fb950" if r.user_edited else "#484f58"),
            ("最后编辑", r.last_edited if r.last_edited else "--", "#8b949e"),
        ]
        for label, val, color in rows_data:
            row = Frame(sf, bg="#425871")
            row.pack(fill=X, padx=8, pady=0)
            Label(row, text=label, font=("微软雅黑", 10), fg="#58a6ff",
                  bg="#425871", width=6, anchor="e").pack(side=LEFT, padx=(0, 6))
            Label(row, text=val, font=("微软雅黑", 10), fg=color,
                  bg="#425871", anchor="w").pack(side=LEFT)

        # 资源元数据（只读）
        Label(w, text="资源元数据（系统自动处理，不可编辑）:", font=("微软雅黑", 11),
              fg="#8b949e", bg="#364b63", anchor="w").pack(fill=X, padx=14, pady=(6, 0))

        meta_frame = Frame(w, bg="#364b63")
        meta_frame.pack(fill=X, padx=14, pady=(2, 6))
        meta_view = Text(meta_frame, font=("Consolas", 10), wrap=WORD,
                         bg="#253747", fg="#8b949e", padx=10, pady=8,
                         bd=1, relief="solid", height=6, highlightthickness=1,
                         highlightcolor="#58a6ff", highlightbackground="#4a6078")
        meta_view.pack(side=LEFT, fill=X, expand=True)
        meta_scroll = Scrollbar(meta_frame, orient=VERTICAL, command=meta_view.yview)
        meta_scroll.pack(side=RIGHT, fill=Y)
        meta_view.config(yscrollcommand=meta_scroll.set)
        meta_view.config(state=NORMAL)
        if r.has_ctx:
            try:
                with open(r.ctx_path, "r", encoding="utf-8") as f:
                    ctx_raw = f.read()
                # 提取 frontmatter + ![[filename]] 部分（去掉上下文）
                parts = ctx_raw.split("---", 2)
                if len(parts) >= 3:
                    fm_text = parts[1]
                    # 获取 ctx 文件修改时间
                    ctx_mtime = ""
                    try:
                        if r.ctx_path.exists():
                            ct = datetime.fromtimestamp(r.ctx_path.stat().st_mtime)
                            ctx_mtime = ct.strftime("%Y-%m-%d %H:%M:%S")
                    except: pass
                    # 补全缺失的字段（按正确顺序）
                    if "importance:" not in fm_text or "user_edited:" not in fm_text or "last_edited_time:" not in fm_text:
                        fm_lines = _ensure_fields_separate(fm_text.split(chr(10)))
                        new_lines = []
                        inserted_imp = False
                        inserted_ue = False
                        for line in fm_lines:
                            new_lines.append(line)
                            if line.strip().startswith("type: resource") and not inserted_imp:
                                new_lines.append("importance: 3")
                                inserted_imp = True
                            if line.strip().startswith("resource_type:") and not inserted_ue:
                                if "user_edited:" not in fm_text:
                                    new_lines.append("user_edited: false")
                                if "last_edited_time:" not in fm_text:
                                    new_lines.append("last_edited_time: " + ctx_mtime)
                                inserted_ue = True
                        # 如果已存在 last_edited_time 但值为空，补上 ctx 文件修改时间
                        if "last_edited_time:" in fm_text:
                            for i, line in enumerate(new_lines):
                                stripped = line.strip()
                                if stripped.startswith("last_edited_time:") and (stripped.endswith(":") or not stripped.split(":", 1)[1].strip()):
                                    new_lines[i] = f"last_edited_time: {ctx_mtime}"
                        fm_text = chr(10).join(new_lines)
                        # 写回文件（确保 --- 独立成行，![[filename]] 存在）
                        body_text = parts[2].lstrip("\n")
                        media_ref = "![[{}]]".format(r.filename)
                        if media_ref not in body_text:
                            body_text = body_text.rstrip("\n") + "\n" + media_ref
                        ctx_raw = parts[0] + "---\n" + fm_text.strip("\n") + "\n---\n" + body_text
                        with open(r.ctx_path, "w", encoding="utf-8") as fw:
                            fw.write(ctx_raw)
                        r.user_edited = False
                    fm = parts[0] + "---" + fm_text + "---"
                    # body 第一行通常是 ![[filename]]
                    body_lines = parts[2].strip().split(chr(10))
                    media_line = ""
                    other_lines = []
                    for line in body_lines:
                        if line.strip().startswith("![[") and not media_line:
                            media_line = line.strip()
                        else:
                            other_lines.append(line)
                    meta_show = fm + chr(10) + media_line
                else:
                    meta_show = ctx_raw
                meta_view.insert("1.0", meta_show.strip())
            except Exception as e:
                meta_view.insert("1.0", f"[读取失败: {e}]")
        else:
            meta_view.insert("1.0", f"[该资源还没有 .ctx 文件]\n文件名: {r.filename}")
        meta_view.config(state=DISABLED)

        # 从 .ctx 文件中直接读取 tags 原始值，确保与元数据显示一致
        tags_from_file = [r.filepath.stem] if not r.has_ctx else (r.tags[:] if r.tags else [])
        if r.has_ctx:
            try:
                with open(r.ctx_path, "r", encoding="utf-8") as _ftag:
                    _raw = _ftag.read()
                # 只在 frontmatter 中查找 tags
                _fm = _raw
                if _raw.startswith("---"):
                    _p = _raw.split("---", 2)
                    if len(_p) >= 3:
                        _fm = _p[1]
                _mtag = re.search(r'^tags:\s*\[\[(.*?)\]\]|^tags:\s*\[(.*?)\]', _fm, re.MULTILINE)
                if _mtag:
                    val = _mtag.group(1) or _mtag.group(2)
                    tags_from_file = [t.strip().strip("[]") for t in val.split(",") if t.strip()]
            except:
                pass

        # 记录初始值，用于检测是否修改
        init_importance = r.importance
        init_tags = ", ".join(tags_from_file)
        init_editor_text = ""

        # 绿色提示文字 + 保存/退出按钮（同一行）
        hint_row = Frame(w, bg="#364b63")
        hint_row.pack(fill=X, padx=14, pady=(4, 0))
        Label(hint_row, text="为提高本资源被采用的命中率，可手动编写下面内容", font=("微软雅黑", 11),
              fg="#3fb950", bg="#364b63", anchor="w", wraplength=600).pack(side=LEFT)

        def exit_check():
            changed = False
            if star_var.get() != init_importance: changed = True
            if tag_var.get().strip() != init_tags: changed = True
            if r.has_ctx and editor.get("1.0", "end-1c").strip() != init_editor_text: changed = True
            if changed:
                if messagebox.askyesno("确认退出", "内容已修改，是否放弃更改并退出？"):
                    w.destroy()
                    return
                w.lift()
                w.focus_force()
            else:
                w.destroy()

        hint_exit_btn = Button(hint_row, text="退出编辑", bg="#da3633", fg="white",
                               relief="flat", padx=14, font=("微软雅黑", 11),
                               command=exit_check)
        hint_exit_btn.pack(side=RIGHT, padx=(6, 0))
        hint_save_btn = Button(hint_row, text="保存", bg="#238636", fg="white",
                               relief="flat", padx=28, font=("微软雅黑", 11))
        hint_save_btn.pack(side=RIGHT)

        # 重要性星级评分（单独成行）
        importance = r.importance
        star_row = Frame(w, bg="#364b63")
        star_row.pack(fill=X, padx=14, pady=(2, 0))
        Label(star_row, text="本资源重要程度（点击星星修改）：", font=("微软雅黑", 11),
              fg="#58a6ff", bg="#364b63").pack(side=LEFT)
        star_btns = []
        star_var = IntVar(value=importance)
        def set_star(val):
            star_var.set(val)
            for i, btn in enumerate(star_btns):
                btn.config(text="★" if i < val else "☆", fg="#d29922" if i < val else "#8b949e")
        for i in range(1, 6):
            btn = Button(star_row, text="★" if i <= importance else "☆",
                        font=("微软雅黑", 14), bd=0, bg="#364b63",
                        fg="#d29922" if i <= importance else "#8b949e",
                        activebackground="#364b63", cursor="hand2",
                        command=lambda v=i: set_star(v))
            btn.pack(side=LEFT, padx=0)
            star_btns.append(btn)

        # 关键词标签（可编辑）
        tag_row = Frame(w, bg="#364b63")
        tag_row.pack(fill=X, padx=14, pady=(2, 0))
        Label(tag_row, text="关键词标签：", font=("微软雅黑", 11),
              fg="#58a6ff", bg="#364b63").pack(side=LEFT)
        def _normalize_tags(text):
            """将各种分隔符统一转为英文逗号，再拆分、去空、去前后空格"""
            normalized = re.sub(r'[，;；、/\\|。#*　\s]+', ',', text)
            return [t.strip() for t in normalized.split(",") if t.strip()]

        tag_var = StringVar(value=", ".join(tags_from_file))
        tag_entry = Entry(tag_row, textvariable=tag_var, font=("微软雅黑", 10),
                          bg="#2f4459", fg="#c9d1d9", insertbackground="#c9d1d9",
                          relief="solid", bd=1, highlightthickness=1,
                          highlightcolor="#58a6ff", highlightbackground="#4a6078")
        tag_entry.pack(side=LEFT, fill=X, expand=True, padx=(6, 0))

        edit_header = Frame(w, bg="#364b63")
        edit_header.pack(fill=X, padx=14, pady=(0, 0))
        Label(edit_header, text="关联信息（.ctx文件中的上下文）：", font=("微软雅黑", 12),
              fg="#58a6ff", bg="#364b63", anchor="w").pack(side=LEFT)

        def save_and_refresh():
            new_body = editor.get("1.0", "end-1c")
            now_str = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            new_tags = _normalize_tags(tag_var.get())
            media_ref = "![[{}]]".format(r.filename)
            if media_ref not in new_body:
                new_body = new_body.rstrip("\n") + "\n" + media_ref
            if not r.has_ctx:
                # 创建新的 .ctx 文件
                ctx_raw = "---\ntype: resource\nresource_type: {}\nimportance: {}\nuser_edited: true\nlast_edited_time: {}\nsource: \"\"\nbelongs_to_chunk: \"\"\nchunk_heading: \"\"\nresource_file: \"{}\"\ntags: [{}]\nbelongs_to:\n---\n{}\n".format(r.res_type, star_var.get(), now_str, r.filename, ', '.join(new_tags), new_body)
                with open(r.ctx_path, "w", encoding="utf-8") as f:
                    f.write(ctx_raw)
                r.has_ctx = True
                r._parse_ctx()
                self._apply_filter()
                w.destroy()
                self._show_detail(r)
                return
            # 保存前先修复文件格式
            _repair_ctx_format(r.ctx_path, r.filename)
            with open(r.ctx_path, "r", encoding="utf-8") as f:
                ctx_full = f.read()
            parts = ctx_full.split("---", 2)
            if len(parts) >= 3:
                fm_lines = _ensure_fields_separate(parts[1].split(chr(10)))
                now_str = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                new_fm = []
                for line in fm_lines:
                    if line.strip().startswith("user_edited:"):
                        new_fm.append("user_edited: true")
                    elif line.strip().startswith("importance:"):
                        new_fm.append(f"importance: {star_var.get()}")
                    elif line.strip().startswith("tags:"):
                        new_tags = _normalize_tags(tag_var.get())
                        new_fm.append(f"tags: [{', '.join(new_tags)}]")
                    elif line.strip().startswith("last_edited_time:"):
                        new_fm.append(f"last_edited_time: {now_str}")
                    else:
                        new_fm.append(line)
                # 去重：拆分合并行后可能出现多个 tags: 行，保留第一个
                seen_tags = False
                deduped = []
                for _l in new_fm:
                    if _l.startswith("tags:"):
                        if seen_tags:
                            continue
                        seen_tags = True
                    deduped.append(_l)
                new_fm = deduped
                # 确保 tags 存在
                if not any(l.startswith("tags:") for l in new_fm):
                    new_tags = _normalize_tags(tag_var.get())
                    new_fm.append(f"tags: [{', '.join(new_tags)}]")
                fm_body = chr(10).join(new_fm).strip("\n")
                ctx_raw = parts[0] + "---\n" + fm_body + "\n---\n" + new_body.lstrip("\n")
            else:
                ctx_raw = new_body
            with open(r.ctx_path, "w", encoding="utf-8") as f:
                f.write(ctx_raw)
            r._parse_ctx()
            # 刷新主窗口
            self._apply_filter()
            w.destroy()
            self._show_detail(r)

        hint_save_btn.config(command=save_and_refresh)

        ef = Frame(w, bg="#364b63")
        ef.pack(fill=BOTH, expand=True, padx=14, pady=(0, 4))

        editor = Text(ef, font=("Consolas", 11), wrap=WORD,
                      bg="#2f4459", fg="#c9d1d9", insertbackground="#c9d1d9",
                      padx=10, pady=10, bd=1, relief="solid",
                      highlightthickness=1, highlightcolor="#58a6ff", highlightbackground="#4a6078")
        editor.pack(fill=BOTH, expand=True, side=LEFT)
        scroll = Scrollbar(ef, orient=VERTICAL, command=editor.yview)
        scroll.pack(side=RIGHT, fill=Y)
        editor.config(yscrollcommand=scroll.set)

        if r.has_ctx:
            try:
                with open(r.ctx_path, "r", encoding="utf-8") as f:
                    ctx_full = f.read()
                # 只提取 --- 后面的上下文部分（去掉 frontmatter 和 ![[filename]]）
                parts = ctx_full.split("---", 2)
                if len(parts) >= 3:
                    body = parts[2]
                else:
                    body = ctx_full
                body_lines = body.strip().split(chr(10))
                # 跳过 ![[filename]] 行，只保留上下文
                body_lines = [l for l in body_lines if not l.strip().startswith("![[")]
                body = chr(10).join(body_lines).strip()
                editor.insert("1.0", body)
                init_editor_text = body
            except Exception as e:
                editor.insert("1.0", f"[读取失败: {e}]")
        else:
            editor.insert("1.0", r.filename)
            init_editor_text = r.filename

        # 底部按钮
        bf = Frame(w, bg="#364b63")
        bf.pack(fill=X, padx=14, pady=(4, 10))

        def save_ctx(ed=editor, res=r):
            new_body = ed.get("1.0", "end-1c")
            now_str = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            new_tags = _normalize_tags(tag_var.get())
            media_ref = "![[{}]]".format(res.filename)
            if media_ref not in new_body:
                new_body = new_body.rstrip("\n") + "\n" + media_ref
            if not res.has_ctx:
                ctx_raw = "---\ntype: resource\nresource_type: {}\nimportance: {}\nuser_edited: true\nlast_edited_time: {}\nsource: \"\"\nbelongs_to_chunk: \"\"\nchunk_heading: \"\"\nresource_file: \"{}\"\ntags: [{}]\nbelongs_to:\n---\n{}\n".format(res.res_type, star_var.get(), now_str, res.filename, ', '.join(new_tags), new_body)
                with open(res.ctx_path, "w", encoding="utf-8") as f:
                    f.write(ctx_raw)
                res.has_ctx = True
                res._parse_ctx()
                self._apply_filter()
                messagebox.showinfo("完成", "已创建 .ctx 文件")
                return
            try:
                with open(res.ctx_path, "r", encoding="utf-8") as f:
                    ctx_full = f.read()
                parts = ctx_full.split("---", 2)
                if len(parts) >= 3:
                    fm_lines = _ensure_fields_separate(parts[1].split(chr(10)))
                    now_str = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                    new_fm = []
                    for line in fm_lines:
                        if line.strip().startswith("user_edited:"):
                            new_fm.append("user_edited: true")
                        elif line.strip().startswith("importance:"):
                            new_fm.append(f"importance: {star_var.get()}")
                        elif line.strip().startswith("tags:"):
                            new_tags = _normalize_tags(tag_var.get())
                            new_fm.append(f"tags: [{', '.join(new_tags)}]")
                        elif line.strip().startswith("last_edited_time:"):
                            new_fm.append(f"last_edited_time: {now_str}")
                        else:
                            new_fm.append(line)
                    if not any(l.startswith("tags:") for l in new_fm):
                        new_tags = _normalize_tags(tag_var.get())
                        new_fm.append(f"tags: [{', '.join(new_tags)}]")
                    ctx_full = parts[0] + "---\n" + chr(10).join(new_fm).strip("\n") + "\n---\n" + new_body.lstrip("\n")
                with open(res.ctx_path, "w", encoding="utf-8") as f:
                    f.write(ctx_full)
                res._parse_ctx()
                self._apply_filter()
                messagebox.showinfo("完成", ".ctx 已保存")
            except Exception as e:
                messagebox.showerror("错误", f"保存失败: {e}")

        Button(bf, text="保存到 .ctx", bg="#238636", fg="white",
               relief="flat", padx=14, font=("微软雅黑", 11),
               command=save_ctx).pack(side=LEFT, padx=2)
        def close_popup():
                w.destroy()
        Button(bf, text="关闭", bg="#21262d", fg="white",
               relief="flat", padx=14, font=("微软雅黑", 11),
               command=close_popup).pack(side=RIGHT, padx=2)

    def _exit_app(self):
        self.root.destroy()

    def _delete_selected(self):
        if not self.selected:
            messagebox.showinfo("提示", "先勾选要删除的资源")
            return
        n = len(self.selected)
        if not messagebox.askyesno("确认", f"删除 {n} 个资源？不可撤销！"):
            return
        ok = 0
        for idx in sorted(self.selected, reverse=True):
            if idx < len(self.filtered):
                if delete_resource(self.filtered[idx]): ok += 1
        messagebox.showinfo("完成", f"已删除 {ok} 个")
        self._refresh()

    def _show_stats(self):
        r = self.all_resources
        t = len(r)
        wc = sum(1 for x in r if x.has_ctx)
        wl = sum(1 for x in r if x.belongs_to)
        ts = sum(x.size_bytes for x in r)
        bt = defaultdict(int)
        be = defaultdict(int)
        for x in r:
            bt[x.res_type] += 1
            be[x.ext] += 1
        msg = (f"资源统计\n{'─'*36}\n总数: {t}\n有.ctx: {wc} ({wc/t*100:.1f}%)\n"
               f"已关联: {wl} ({wl/t*100:.1f}%)\n"
               f"总大小: {ts/1024/1024:.1f} MB\n\n"
               f"类型: {dict(bt)}\n格式: {dict(sorted(be.items(),key=lambda x:-x[1]))}")
        messagebox.showinfo("资源统计", msg)

    def run(self):
        self.root.mainloop()


def _set_app_state(state):
    """在注册表中记录程序状态：空=未运行, running=运行中, completed=已退出"""
    try:
        import winreg
        key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, "Environment", 0,
                             winreg.KEY_SET_VALUE)
        winreg.SetValueEx(key, "AHKB_MANAGER_STATE", 0, winreg.REG_SZ, state)
        winreg.CloseHandle(key)
        # 广播环境变量变更通知
        try:
            import ctypes
            HWND_BROADCAST = 0xFFFF
            WM_SETTINGCHANGE = 0x001A
            ctypes.windll.user32.SendMessageTimeoutW(
                HWND_BROADCAST, WM_SETTINGCHANGE, 0, "Environment", 2, 5000)
        except: pass
    except: pass


def main():
    """启动资源管理器 GUI。退出后写入状态文件。"""
    # ── 统计初始资源 ──
    initial_count = 0
    if RES_BASE and RES_BASE.exists():
        initial_count = sum(1 for _ in RES_BASE.rglob("*") if _.is_file())

    _set_app_state("running")
    if not RES_BASE or not RES_BASE.exists():
        print(f"错误: 未找到资源目录。请使用 --workspace 指定知识库路径。")
        _set_app_state("completed")
        sys.exit(1)
    try:
        app = ResourceManagerGUI()
        app.run()
    finally:
        _set_app_state("completed")
        # 始终写入状态文件（固定路径，LLM 轮询用）
        result_file = VAULT / "临时工作文件" / "_resource_manager_result.json" if VAULT else None
        if result_file:
            try:
                final_count = 0
                if RES_BASE and RES_BASE.exists():
                    final_count = sum(1 for _ in RES_BASE.rglob("*") if _.is_file())
                delta = final_count - initial_count
                result_data = {
                    "status": "closed",
                    "initial_resources": initial_count,
                    "final_resources": final_count,
                    "resources_delta": delta,
                    "timestamp": datetime.now().isoformat(),
                }
                result_file.parent.mkdir(parents=True, exist_ok=True)
                result_file.write_text(json.dumps(result_data, ensure_ascii=False), encoding="utf-8")
            except Exception:
                pass

if __name__ == "__main__":
    ws_arg = None
    if "--workspace" in sys.argv:
        idx = sys.argv.index("--workspace")
        if idx + 1 < len(sys.argv):
            ws_arg = sys.argv[idx + 1]
    resolve_vault(ws_arg)
    print(f"\n📂 知识库路径: {VAULT}")
    print("🖐  正在启动资源管理器界面...\n")
    main()
    print("✅ 资源管理已完成。\n")
