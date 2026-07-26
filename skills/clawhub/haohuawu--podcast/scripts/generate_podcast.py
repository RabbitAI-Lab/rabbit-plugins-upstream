#!/usr/bin/env python3
# /// script
# requires-python = ">=3.9"
# dependencies = ["requests", "tos", "markdown"]
# ///
"""podcast 技能主入口：脚本 Markdown → 音频 → 发布到 TOS 并更新 RSS feed。

依赖自包含：环境缺 requests/tos 时用 `uv run scripts/generate_podcast.py ...`
（PEP 723 内联元数据自动解析依赖），无需任何本地项目或预建 venv。

用法:
  python3 generate_podcast.py --init --config filled.json --cover cover.png   # 首次初始化（config+封面上 TOS）
  python3 generate_podcast.py --script script.md --slug 20260715_my_episode --dry-run
  python3 generate_podcast.py --script script.md --slug 20260715_my_episode --notes notes.md
  python3 generate_podcast.py --script script.md --slug 20260715_my_episode --no-upload
  python3 generate_podcast.py --script script.md --slug 20260715_my_episode --force  # 忽略缓存重合成

TOS 定位走环境变量：TOS_BUCKET / TOS_REGION / TOS_ACCESS_KEY / TOS_SECRET_KEY。
状态事实源在 TOS（跨环境无状态），key 常量见 podcast_store.py。

幂等约定：slug 是单集的稳定主键——本地目录、TOS 对象 key、RSS guid、episodes.json
记录全部由它派生。同一 slug 重跑 = 覆盖同一单集（小宇宙不会新增重复单集）。

断点恢复：$TMPDIR/podcasts/{slug}/（PODCAST_WORKDIR 可覆盖）缓存分片 WAV（内容 md5 为 key）
与 manifest（脚本/音频 md5 + 阶段时间戳）。中途失败重跑不重复已完成的 TTS 工作；
--force 全部重来。
"""

import argparse
import hashlib
import json
import os
import re
import shutil
import sys
import tempfile
from datetime import datetime, timezone, timedelta
from pathlib import Path

SKILL_DIR = Path(__file__).parent.parent
# 本地状态/产物根目录：默认 tempfile.gettempdir()/podcasts（Linux 即 /tmp/podcasts，
# macOS 是 per-user 的 $TMPDIR/podcasts；宿主无关，不污染 cwd），PODCAST_WORKDIR
# 可覆盖。断点缓存与构建产物同居一目录：{PODCAST_DIR}/{slug}/。
PODCAST_DIR = Path(os.environ.get("PODCAST_WORKDIR") or str(Path(tempfile.gettempdir()) / "podcasts"))
CST = timezone(timedelta(hours=8))

SLUG_RE = re.compile(r"^\d{8}_[a-z0-9]+(_[a-z0-9]+)*$")

sys.path.insert(0, str(Path(__file__).parent))
from script_md import is_host, is_narration, parse_podcast_script, read_title
from script_synthesis import (DoubaoTTS, chunk_cache_key, generate_podcast_audio,
                              get_duration_seconds, resolve_voices)
from podcast_store import (CONFIG_KEY, PREFIX, build_description, fetch_config,
                           fetch_episodes, publish_state, upsert_episode)
from tos_uploader import TOSUploader


def validate_config(instance: dict) -> dict:
    """按 assets/config.schema.json 校验频道配置实例（轻量校验，无 jsonschema 依赖）。
    通过则返回补齐 default 后的配置；失败打印明细并退出。"""
    schema_path = SKILL_DIR / "assets" / "config.schema.json"
    with open(schema_path, encoding="utf-8") as f:
        schema = json.load(f)
    props = schema["properties"]

    errors = []
    for field in schema.get("required", []):
        value = instance.get(field)
        if not isinstance(value, str) or not value.strip():
            errors.append(f"{field}: 必填非空字符串 —— {props[field]['description']}")
    for field in instance:
        if field not in props:
            errors.append(f"{field}: schema 未定义的字段")
    if isinstance(instance.get("email"), str) and instance.get("email") and "@" not in instance["email"]:
        errors.append("email: 不是合法邮箱")
    if isinstance(instance.get("site_url"), str) and instance.get("site_url") \
            and not instance["site_url"].startswith(("http://", "https://")):
        errors.append("site_url: 必须是 http(s) URL")
    if errors:
        print(f"❌ 频道配置不符合 {schema_path.name}：")
        for e in errors:
            print(f"   - {e}")
        print("   请按 schema 向用户逐项确认真实值后重试，不要编造默认值。")
        sys.exit(1)

    for field, spec in props.items():
        if field not in instance and "default" in spec:
            instance[field] = spec["default"]
    return instance


def cmd_init(config_path: str, cover_path: str = None):
    """首次初始化：校验配置实例，上传配置与封面到 TOS，建立远端事实源。"""
    path = Path(config_path)
    if not path.exists():
        print(f"❌ 配置实例不存在: {path}（按 assets/config.schema.json 收集用户真实值后写成 JSON）")
        sys.exit(1)
    with open(path, encoding="utf-8") as f:
        config = validate_config(json.load(f))

    # 封面是频道私有素材，不随 skill 分发：--cover 显式指定；assets/cover.png 仅本地开发兜底
    cover = Path(cover_path).expanduser() if cover_path else SKILL_DIR / "assets" / "cover.png"
    if not cover.exists():
        print(f"❌ 封面不存在: {cover}")
        print("   请用 --cover /path/to/cover.png 指定一张 1400-3000px 方图 PNG 后重跑")
        sys.exit(1)

    uploader = TOSUploader()

    # 封面用带日期的文件名上传，避免平台缓存
    cover_filename = f"cover_{datetime.now(CST).strftime('%Y%m%d')}.png"
    cover_key = f"{PREFIX}{cover_filename}"
    cover_url = uploader.upload_file(str(cover), cover_key, content_type="image/png")
    config["cover_url"] = cover_url
    config_url = uploader.upload_text(
        json.dumps(config, ensure_ascii=False, indent=2),
        CONFIG_KEY, content_type="application/json; charset=utf-8",
        cache_control="no-cache, max-age=60")
    print(f"✅ 频道配置: {config_url}")
    print(f"✅ 封面: {cover_url}")
    print(f"\n初始化完成。feed 将位于 {uploader.base_url}/podcasts/feed.xml（首期发布后生成）。")


# ===== 任务工作目录与断点恢复（key = slug）=====
# {PODCAST_DIR}/{slug}/ 缓存中间产物：分片 WAV 缓存 + manifest（脚本/音频 md5 + 阶段时间戳）。
# 一切中间产物以内容 md5 保证幂等：中途失败重跑不重复已完成的工作；--force 全部重来。

def workdir_for(slug: str) -> Path:
    # env 动态重读：生产环境在进程启动前设置，与 import 期的 PODCAST_DIR 恒一致；
    # 测试/嵌入式场景可能在 import 后才 monkeypatch env，这里兜底兼容。
    d = Path(os.environ.get("PODCAST_WORKDIR") or str(PODCAST_DIR)) / slug
    d.mkdir(parents=True, exist_ok=True)
    return d


def file_md5(path) -> str:
    h = hashlib.md5()
    with open(path, "rb") as f:
        for block in iter(lambda: f.read(1 << 20), b""):
            h.update(block)
    return h.hexdigest()


def load_manifest(workdir: Path) -> dict:
    p = workdir / "manifest.json"
    if p.exists():
        try:
            return json.loads(p.read_text(encoding="utf-8"))
        except (json.JSONDecodeError, OSError):
            pass  # 损坏的 manifest 等同不存在：最多多做一次工作，不会做错
    return {}


def save_manifest(workdir: Path, manifest: dict):
    p = workdir / "manifest.json"
    tmp = p.with_suffix(".json.tmp")
    tmp.write_text(json.dumps(manifest, ensure_ascii=False, indent=2), encoding="utf-8")
    tmp.replace(p)


def synthesis_fingerprint(args) -> str:
    """合成参数指纹：音色/语速/语气/静音/垫乐/后处理任一变化都要触发重新合成——
    manifest 只看脚本 md5 会在换音色后错误复用旧音频。"""
    from script_md import (NARRATION_CONTEXT_TEXTS, NARRATION_GAIN_DB,
                           NARRATION_LEAD_SILENCE_MS, NARRATION_SPEECH_RATE,
                           NARRATION_TAIL_SILENCE_MS, NORMAL_SILENCE_MS)
    from script_synthesis import CACHE_VER, NARRATION_RADIO_FILTER, narration_tap_file
    host, guest = resolve_voices(args.host_voice, args.guest_voice)
    tap_path = (narration_tap_file()
                if os.environ.get("PODCAST_NARRATION_TAP") != "off" else None)
    tap_md5 = file_md5(tap_path) if tap_path else ""
    raw = "|".join(map(str, [
        CACHE_VER, host, guest, NARRATION_SPEECH_RATE, NARRATION_GAIN_DB,
        NARRATION_LEAD_SILENCE_MS, NARRATION_TAIL_SILENCE_MS, NORMAL_SILENCE_MS,
        ";".join(NARRATION_CONTEXT_TEXTS),
        NARRATION_RADIO_FILTER, tap_md5,
        not args.no_postprocess,
    ]))
    return hashlib.md5(raw.encode("utf-8")).hexdigest()


def audio_reusable(manifest: dict, script_md5: str, audio_path: str, params_fp: str) -> bool:
    """脚本没变、合成参数没变、本地 MP3 与 manifest 记录一致 → 复用，跳过整轮 TTS。"""
    rec = manifest.get("audio") or {}
    return (manifest.get("script_md5") == script_md5
            and manifest.get("synthesis_params") == params_fp
            and os.path.exists(audio_path)
            and rec.get("md5") == file_md5(audio_path))


def preflight(args, script_path: Path) -> list:
    """第一次 TTS 调用之前验明一切，一次性列出全部问题（fail-fast，别让钱先花出去）。"""
    errors = []
    for binary in ("ffmpeg", "ffprobe"):
        if not shutil.which(binary):
            errors.append(f"{binary} 不在 PATH（音频处理必需）")
    if not parse_podcast_script(str(script_path)):
        errors.append("脚本未解析到任何对话段（检查 **主持人**：/**嘉宾**：/**旁白**： 格式）")
    if not os.environ.get("DOUBAO_TTS_API_KEY"):
        errors.append("缺少 DOUBAO_TTS_API_KEY 环境变量（TTS 必需）")
    if args.notes and not Path(args.notes).exists():
        errors.append(f"--notes 文件不存在: {args.notes}")

    # ===== 格式校验内联（EP1/EP12 类格式事故在花钱之前拦住）=====
    if not args.skip_validate:
        from validate_podcast import validate_notes, validate_script
        issues = validate_script(str(script_path))
        if args.notes and Path(args.notes).exists():
            issues += validate_notes(args.notes)
        if issues:
            errors.append(f"格式校验未通过 {len(issues)} 项（确认误报可用 --skip-validate 跳过）：")
            errors.extend(f"  · {i}" for i in issues)

    # ===== notes 政策（EP6 两类事故代码化）=====
    if not args.no_upload:
        if not args.notes and not args.no_notes:
            errors.append("发布必须提供 --notes notes.md（否则 RSS description 退化为纯标题）；"
                          "确要放弃请显式传 --no-notes")
        if args.notes and Path(args.notes).exists():
            if Path(args.notes).name == "article.md":
                errors.append("--notes 收到 article.md：它是长文留档，绝不能进 RSS description"
                              "（EP6 教训，15067 字符全文上了小宇宙）；请传 notes.md")
            elif len(build_description("", args.notes)) > 8000:
                # 阈值经真实数据校准：富链接 shownotes 实测 ~5700 字符（放行），
                # EP6 误传全文事故为 15067 字符（拦截）
                errors.append(f"notes 渲染后超过 8000 字符：疑似传了全文而非 shownotes"
                              f"（EP6 教训，全文 15067 字符上了小宇宙）；请精简或确认文件传对了")
    if not args.no_upload:
        missing = [v for v in ("TOS_ACCESS_KEY", "TOS_SECRET_KEY", "TOS_BUCKET", "TOS_REGION")
                   if not os.environ.get(v)]
        if missing:
            errors.append(f"缺少 TOS 环境变量: {', '.join(missing)}（发布必需；--no-upload 可跳过）")
        else:
            try:
                if TOSUploader().download_text(CONFIG_KEY) is None:
                    errors.append(f"TOS 上没有 {CONFIG_KEY}：先执行 --init 完成首次初始化")
            except Exception as e:
                errors.append(f"TOS 连接失败: {e}")
    return errors


def cmd_dry_run(args, script_path: Path):
    """计费预估（免费）：口径 = preprocess 后实发文本；报告分片缓存命中后的净计费。"""
    segments = parse_podcast_script(str(script_path))
    host_voice, guest_voice = resolve_voices(args.host_voice, args.guest_voice)
    cache_dir = workdir_for(args.slug) / "clips_cache"
    billable = cached = 0
    for speaker, text in segments:
        narration = is_narration(speaker)
        voice = host_voice if (narration or is_host(speaker)) else guest_voice
        for chunk in DoubaoTTS.split_long_text(DoubaoTTS.preprocess_text(text)):
            billable += len(chunk)
            if (cache_dir / f"{chunk_cache_key(chunk, voice, narration)}.wav").exists():
                cached += len(chunk)
    print(f"解析到 {len(segments)} 段，计费口径共 {billable} 字符（preprocess 后实发文本）")
    if cached:
        print(f"分片缓存命中 {cached} 字符，本次预计净计费 {billable - cached} 字符")
    for i, (speaker, text) in enumerate(segments[:8]):
        print(f"  [{i+1}] {speaker}: {text[:50]}{'...' if len(text) > 50 else ''}")
    if len(segments) > 8:
        print(f"  ... 共 {len(segments)} 段")


def cmd_run(args, script_path: Path):
    """合成（带断点恢复）+ 发布。"""
    # ===== preflight：第一次 TTS 调用之前验明一切（fail-fast）=====
    problems = preflight(args, script_path)
    if problems:
        print("❌ preflight 检查未通过（先修复再跑，别让 TTS 的钱白花）：")
        for p in problems:
            print(f"   - {p}")
        sys.exit(1)

    title = read_title(script_path)
    out_dir = PODCAST_DIR / args.slug
    out_dir.mkdir(parents=True, exist_ok=True)

    dest_script = out_dir / "script.md"
    if dest_script.resolve() != script_path.resolve():
        dest_script.write_text(script_path.read_text(encoding="utf-8"), encoding="utf-8")

    # ===== 合成：脚本没变且 MP3 完好 → 直接复用，零 TTS 调用 =====
    workdir = workdir_for(args.slug)
    manifest = load_manifest(workdir)
    script_md5 = file_md5(dest_script)
    params_fp = synthesis_fingerprint(args)
    output_audio = str(out_dir / "podcast.mp3")

    if not args.force and audio_reusable(manifest, script_md5, output_audio, params_fp):
        print(f"↻ 复用已合成音频（脚本与合成参数未变更，合成于 "
              f"{manifest.get('stages', {}).get('synthesized', '?')}）"
              f"——跳过 TTS；--force 可强制重新合成")
    else:
        tts = DoubaoTTS(host_voice=args.host_voice, guest_voice=args.guest_voice)
        result = generate_podcast_audio(
            str(dest_script), output_audio, tts, postprocess=not args.no_postprocess,
            cache_dir=str(workdir / "clips_cache"), force=args.force,
        )
        if result is None:
            sys.exit(1)  # 失败即中止：绝不带着缺失内容进入发布
        manifest["script_md5"] = script_md5
        manifest["synthesis_params"] = params_fp
        manifest["audio"] = {"path": output_audio, "md5": file_md5(output_audio)}
        manifest.setdefault("stages", {})["synthesized"] = datetime.now(CST).isoformat()
        save_manifest(workdir, manifest)

    if args.no_upload:
        print(f"\n--no-upload：跳过发布。试听通过后用相同 slug 重跑（不带 --no-upload）即可发布"
              f"——脚本未变更时直接复用本次音频，不再重新计费。")
        return

    # ===== 发布：拉远端状态 → 传音频/文档 → 回传状态（顺序由 podcast_store 固化）=====
    uploader = TOSUploader()
    config = fetch_config(uploader)
    if config is None:
        print(f"❌ TOS 上没有 {CONFIG_KEY}。先执行 --init 完成首次初始化。")
        sys.exit(1)
    episodes = fetch_episodes(uploader)

    file_hash = file_md5(output_audio)[:6]
    audio_key = f"{PREFIX}episodes/{args.slug}/podcast_{file_hash}.mp3"
    print(f"\n上传音频: {audio_key}")
    audio_url = uploader.upload_file(output_audio, audio_key, content_type="audio/mpeg")
    print(f"  ✅ {audio_url}")

    # ===== 上传 script.md + notes.md 到 episodes/{slug}/ 留档 =====
    episode_dir = Path(args.script).parent
    slug_dir_key = f"{PREFIX}episodes/{args.slug}/"
    for fname in ("script.md", "notes.md", "article.md"):
        fpath = episode_dir / fname
        if fpath.exists():
            key = f"{slug_dir_key}{fname}"
            uploader.upload_text(
                fpath.read_text(encoding="utf-8"),
                key,
                content_type="text/markdown; charset=utf-8",
            )
            print(f"  ✅ {fname} -> {key}")

    # ===== 上传 images/ 到 episodes/{slug}/images/ =====
    images_dir = episode_dir / "images"
    if images_dir.is_dir():
        for img in sorted(images_dir.iterdir()):
            suffix = img.suffix.lower()
            if img.is_file() and suffix in (".png", ".jpg", ".jpeg", ".gif", ".webp"):
                ct = {".png": "image/png", ".jpg": "image/jpeg", ".jpeg": "image/jpeg",
                      ".gif": "image/gif", ".webp": "image/webp"}.get(suffix, "image/jpeg")
                key = f"{slug_dir_key}images/{img.name}"
                uploader.upload_file(str(img), key, content_type=ct)
                print(f"  ✅ images/{img.name} -> {key}")

    if not args.notes:
        print("⚠️ 未提供 --notes，RSS description 将退化为仅标题——发布前应写好 notes.md（见 SKILL.md Shownotes spec）")
    description = build_description(title, args.notes or None)

    new_episode = {
        "slug": args.slug,
        "title": title,
        "description": description,
        "audio_url": audio_url,
        "audio_size": os.path.getsize(output_audio),
        "duration": get_duration_seconds(output_audio),
        "pub_date": datetime.now(CST).isoformat(),
        "episode_num": max((ep.get("episode_num", 0) for ep in episodes), default=0) + 1,
    }
    episodes = upsert_episode(episodes, new_episode)

    rss_url = publish_state(uploader, config, episodes,
                            target_slug=args.slug, force_state=args.force_state)
    print(f"  ✅ RSS feed: {rss_url}")

    manifest.setdefault("stages", {})["published"] = datetime.now(CST).isoformat()
    save_manifest(workdir, manifest)

    ep = new_episode
    print(f"\n{'=' * 60}")
    print("播客发布完成")
    print(f"{'=' * 60}")
    print(f"  音频 URL: {audio_url}")
    print(f"  RSS Feed: {rss_url}")
    print(f"  时长: {ep['duration']}s ({ep['duration']/60:.1f} min)  期号: EP{ep['episode_num']}")
    print(f"\n首次发布：在小宇宙主播后台提交 RSS URL 认领（验证码发往 config 中的 email）；")
    print(f"后续新单集自动被抓取。同一集修正后重跑相同 slug 即可覆盖，不会产生重复单集。")


def main():
    parser = argparse.ArgumentParser(description="播客生成与发布（状态事实源在 TOS podcasts/ 下）")
    parser.add_argument("--init", action="store_true",
                        help="首次初始化：校验 --config 实例并上传配置+封面到 TOS")
    parser.add_argument("--config",
                        help="频道配置 JSON 实例路径（按 assets/config.schema.json 收集），仅 --init 用")
    parser.add_argument("--cover",
                        help="频道封面 PNG 路径（1400-3000px 方图；私有素材不随 skill 分发），仅 --init 用")
    parser.add_argument("--script", help="播客脚本 Markdown 路径")
    parser.add_argument("--slug",
                        help="单集稳定标识，格式 YYYYMMDD_english_words（决定目录/对象 key/guid，发布后不可变）")
    parser.add_argument("--notes", help="单集 shownotes 文本文件（进 RSS description），缺省用标题")
    parser.add_argument("--host-voice", help="主持人音色 ID")
    parser.add_argument("--guest-voice", help="嘉宾音色 ID")
    parser.add_argument("--no-upload", action="store_true",
                        help="只合成不发布（试听/调试用）；默认合成后即发布")
    parser.add_argument("--no-postprocess", action="store_true", help="跳过音频后处理")
    parser.add_argument("--dry-run", action="store_true", help="只解析脚本统计字符数（计费预估），不调 TTS")
    parser.add_argument("--force", action="store_true",
                        help="忽略工作目录里的合成结果与分片缓存，强制全部重新合成")
    parser.add_argument("--force-state", action="store_true",
                        help="跳过发布前的线上状态 diff 守卫（除目标单集外其余必须不变）；"
                             "仅预期中的批量迁移使用")
    parser.add_argument("--no-notes", action="store_true",
                        help="显式声明不带 shownotes 发布（RSS description 退化为纯标题）")
    parser.add_argument("--skip-validate", action="store_true",
                        help="跳过合成前的 script/notes 格式校验（仅确认误报时使用）")
    args = parser.parse_args()

    if args.init:
        if not args.config:
            parser.error("--init 需要 --config <频道配置 JSON 实例>")
        cmd_init(args.config, args.cover)
        return

    if not args.script or not args.slug:
        parser.error("--script 与 --slug 必填（或用 --init 做首次初始化）")
    if not SLUG_RE.match(args.slug):
        print(f"❌ slug 格式错误: {args.slug}（应为 YYYYMMDD_english_words，如 20260715_my_episode）")
        sys.exit(1)

    script_path = Path(args.script)
    if not script_path.exists():
        print(f"❌ 脚本文件不存在: {script_path}")
        sys.exit(1)

    if args.dry_run:
        cmd_dry_run(args, script_path)
        return

    cmd_run(args, script_path)


if __name__ == "__main__":
    main()
