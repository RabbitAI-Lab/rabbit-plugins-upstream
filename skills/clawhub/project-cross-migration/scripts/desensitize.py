# This file is part of project-cross-migration v2.4.2 free version
# 完整版功能：分享包脱敏器（--share）
# 获取完整版：<https://wzyp.cn/item/p0r2lb>
import sys
print("🚫 完整版功能：分享包脱敏器（--share）。获取完整版：<https://wzyp.cn/item/p0r2lb>")
sys.exit(1)

#!/usr/bin/env python3
"""desensitize.py — 分享包脱敏器（project-cross-migration v2.4.0）

定位（v2.2 重定位）:
  脱敏是**可选分享配件**，不是迁移必经步骤。
  - 私有备份 / 本机还原 / 自己换机：**默认完全不脱敏**，凭据原样随包，恢复即用。
  - 仅当用户主动要求"生成分享包"（把资料包发给他人 / 发布示例）时，才脱敏。

用法:
  1) 单文件脱敏（分享场景）:
       python3 desensitize.py --share <input> <output> [--manifest m]
  2) 整目录 → 分享包（输出 _share/ 脱敏副本 + _credentials_needed.md 缺口清单）:
       python3 desensitize.py --share --package <src_dir> --out-dir <out_dir> [--manifest m]

  不加 --share 直接拒绝执行（退出码 2）并说明原因——防止"顺手脱敏"把私有包的凭据改坏。

原则:
  占位符带 sha256 前 4 位指纹：同一原值 → 同一占位符（可对账）、不可逆。
  映射清单（占位符 ↔ 原值指纹）只留本地，不随分享包走。
  v2.1.1 修复：manifest 键先经 m.expand 展开，与正文占位符完全一致（F2）。
  v2.2.0 修复（F9）：中文/全角字符紧邻敏感值时 `\\b` 词边界失效
    （Python 3 中 CJK 属 \\w，'apikey是sk-xxxx' 里 sk 前取不到 \\b），
    apikey / email / openid 三类正则的开头 `\\b` 改为负向断言 (?<![A-Za-z0-9])。
  v2.2.1 修复（P3-N3/N4）：本机路径规则扩盖——
    winpath 从仅 C:\\Users 扩为任意盘符（大小写不敏感）：用户目录段
    （users/home/documents/desktop）折叠首段保留尾部；其它盘符路径（如 D:\\data\\…）
    也折叠首段（盘符路径本身暴露机器目录结构/用户名，分享场景一律脱）；
    新增 linuxpath 规则 /home/<name> 折叠为 ~。
  已知取舍（F6）：homepath/winpath 统一折叠为 ~（无指纹）——隐私更强，
    但路径类不参与占位符对账；需要可对账时改用 ~user<hash4> 形态。

支持输入: .jsonl（逐行处理）/ .md / .txt / .json（整体处理）
"""
import hashlib
import json
import os
import re
import shutil
import sys

VERSION = "2.4.0"
TEXT_EXT = (".jsonl", ".md", ".txt", ".json")
SKIP_DIRS = {".git", "__pycache__", "_share", ".idea", ".vscode"}
SKIP_FILES = {".DS_Store"}
# 分享包内需要接收方自备的凭据类（对应 _credentials_needed.md）
CREDENTIAL_TYPES = {"apikey", "assign"}


def h4(s: str) -> str:
    return hashlib.sha256(s.encode("utf-8")).hexdigest()[:4]


RULES = [
    # (类型, 识别正则, 替换模板; {h}=指纹, \g<N>=保留分组)
    # v2.2.0：开头 \b 一律改 (?<![A-Za-z0-9])，修复中文/全角紧邻时词边界失效（F9）
    ("apikey",  re.compile(r"(?<![A-Za-z0-9])((?:sk|vda|rk)[-_][A-Za-z0-9]{10,})"), "KEY***{h}"),
    # assign 规则兼容 JSON 转义引号（token=\"...\"）与裸写（token=...）两种形态（F3）
    ("assign",  re.compile(r"(?i)((?:api[_-]?key|token|secret|password)(?:\\?[\"':=\s])+\\?[\"']?)([A-Za-z0-9._-]{12,})"), r"\g<1>***{h}"),
    ("mobile",  re.compile(r"(?<!\d)(1[3-9]\d{9})(?!\d)"), "1**phone{h}"),
    ("email",   re.compile(r"(?<![A-Za-z0-9])([A-Za-z0-9._%+-])[A-Za-z0-9._%+-]*(@[A-Za-z0-9.-]+\.[A-Za-z]{2,})"), r"\g<1>***{h}\g<2>"),
    ("openid",  re.compile(r"(?<![A-Za-z0-9])((?:ou_|u_|on_))([0-9a-f]{8,})"), r"\g<1>***{h}"),
    ("homepath", re.compile(r"/Users/[^/\s\"']+"), "~"),
    # v2.2.1（P3-N3）：盘符路径脱敏扩盖。实测缺陷：原规则只护 C:\\Users，
    #   D:\\data\\y.json 原样输出——盘符路径本身就暴露机器目录结构/用户名，
    #   分享场景一律折叠首段（与 /Users/<name> → ~ 同语义，尾部保留）。
    #   ① 用户目录段：users/home/documents/desktop（任意盘符，大小写不敏感）
    #   ② 其它盘符首段：任意盘符 + 任意首段（覆盖 D:\\data\\… 这类自定义目录）
    ("winpath", re.compile(r"(?i)[a-z]:\\{1,2}(?:users|home|documents|desktop)\\{1,2}[^\\\s\"\']+"), "~"),  # v2.2.1 N3: users/home 段（兼容 JSONL 双反斜杠转义）
    ("winpath", re.compile(r"(?i)[a-z]:\\{1,2}[^\\\s\"\']+"), "~"),  # v2.2.1 N3: 任意盘符任意首段（含转义形态）
    # v2.2.1（P3-N4）：Linux home 路径折叠为 ~
    ("linuxpath", re.compile(r"/home/[^/\s\"']+"), "~"),
]


def _load_manifest(mf):
    if mf and os.path.exists(mf):
        with open(mf, encoding="utf-8") as f:
            return json.load(f)
    return {}


def _save_manifest(mf, manifest):
    if not mf:
        return
    with open(mf, "w", encoding="utf-8") as f:
        json.dump(manifest, f, ensure_ascii=False, indent=2)


def apply_rules(text, manifest, source, hits=None):
    """对文本执行全部脱敏规则；按类型累计命中次数（hits）。"""
    for name, pat, tmpl in RULES:
        def _sub(m, name=name, tmpl=tmpl):
            rep = tmpl.replace("{h}", h4(m.group(0)))
            final = m.expand(rep)  # 先展开分组引用，manifest 键与正文占位符保持一致（F2 修复）
            manifest.setdefault(final, {
                "type": name,
                "sha256_12": hashlib.sha256(m.group(0).encode("utf-8")).hexdigest()[:12],
                "first_seen": source,
            })
            if hits is not None:
                hits[name] = hits.get(name, 0) + 1
            return final
        text = pat.sub(_sub, text)
    return text


def desensitize_text_file(src, dst, manifest, hits=None):
    """脱敏单个文本文件；返回命中行数（jsonl）/ 行数（整体文件）。"""
    with open(src, encoding="utf-8") as f:
        content = f.read()
    is_jsonl = src.endswith(".jsonl")
    lines = content.splitlines() if is_jsonl else [content]
    masked = 0
    out_lines = []
    for idx, line in enumerate(lines, 1):
        before = line
        line = apply_rules(line, manifest, f"{os.path.basename(src)}:L{idx}", hits)
        if line != before:
            masked += 1
        out_lines.append(line)
    os.makedirs(os.path.dirname(os.path.abspath(dst)) or ".", exist_ok=True)
    sep = "\n" if is_jsonl else ""
    with open(dst, "w", encoding="utf-8") as f:
        f.write(sep.join(out_lines) + ("\n" if is_jsonl else ""))
    return masked


def write_credentials_needed(out_dir, hits, manifest):
    """分享包专用：被脱敏的凭据类缺口清单（接收方需自备）。"""
    cred_lines = []
    for name in sorted(CREDENTIAL_TYPES):
        n = hits.get(name, 0)
        if n:
            samples = [k for k, v in manifest.items() if v.get("type") == name][:3]
            cred_lines.append(f"- **{name}**：{n} 处已替换为占位符（示例：{'、'.join(samples) if samples else '—'}）")
    body = ["# 分享包凭据缺口清单（_credentials_needed.md）", "",
            "> 本文件仅由**分享包**生成。私有备份 / 本机还原 / 换机场景**默认不脱敏**，",
            "> 凭据原样随包、恢复即用，不会出现本文件。", ""]
    if cred_lines:
        body += ["本分享包中以下凭据类内容已被替换为占位符，接收方需在目标框架自行配置：", ""]
        body += cred_lines
    else:
        body += ["本次脱敏未命中凭据类内容（仅命中手机号/邮箱/用户ID/本机路径等），接收方无需额外配置凭据。"]
    body += ["", "## 说明", "",
             "- 占位符 `<hash4>` = 原值 sha256 前 4 位：同一原值 → 同一占位符（可对账），不可逆。",
             "- 映射清单 `_desensitize_map.json` 只留本地，**不随分享包走**，原值无法从占位符恢复。",
             "- 真实凭据请通过私密渠道单独传递，不要回填进分享包。"]
    path = os.path.join(out_dir, "_credentials_needed.md")
    with open(path, "w", encoding="utf-8") as f:
        f.write("\n".join(body) + "\n")
    return path


def make_share_package(src_dir, out_dir, manifest, mf):
    """整目录 → 分享包：_share/ 脱敏副本 + _credentials_needed.md。"""
    share_dir = os.path.join(out_dir, "_share")
    os.makedirs(share_dir, exist_ok=True)
    hits, copied, binaries, masked_files = {}, 0, [], 0
    for root, dirs, files in os.walk(src_dir):
        dirs[:] = [d for d in dirs if d not in SKIP_DIRS]
        for fn in sorted(files):
            if fn in SKIP_FILES or fn.endswith((".pyc", ".pyo")) or fn.startswith("_desensitize_map"):
                continue
            sp = os.path.join(root, fn)
            dp = os.path.join(share_dir, os.path.relpath(sp, src_dir))
            if fn.endswith(TEXT_EXT):
                desensitize_text_file(sp, dp, manifest, hits)
                masked_files += 1
            else:
                # 非文本（图片/二进制）原样复制；截图可能含敏感信息，登记待人工确认
                os.makedirs(os.path.dirname(dp) or ".", exist_ok=True)
                shutil.copy2(sp, dp)
                binaries.append(os.path.relpath(sp, src_dir))
            copied += 1
    cred_path = write_credentials_needed(out_dir, hits, manifest)
    print(f"分享包已生成: {out_dir}")
    print(f"  - 脱敏副本目录: {share_dir}（{copied} 文件，其中文本 {masked_files} 个已过脱敏）")
    print(f"  - 占位符 {len(manifest)} 种 / 命中 {sum(hits.values())} 处：{hits or '无'}")
    print(f"  - 凭据缺口清单: {cred_path}")
    if binaries:
        print(f"  - ⚠️ 非文本文件 {len(binaries)} 个原样复制（截图/图片可能含敏感信息，需人工确认）: "
              f"{', '.join(binaries[:5])}{' …' if len(binaries) > 5 else ''}")
    print(f"  - 映射清单（只留本地，勿随包）: {mf}")
    return 0


def main():
    print(f"desensitize.py v{VERSION} · 分享包脱敏器（需显式 --share）")
    argv = sys.argv[1:]
    if not argv or "--help" in argv or "-h" in argv or len(argv) < 3:
        print(__doc__)
        sys.exit(2)

    if "--share" not in argv:
        print("[拒绝执行] 默认不脱敏：私有备份 / 本机还原 / 换机场景凭据原样随包、恢复即用。", file=sys.stderr)
        print("            确需生成分享包（发给他人 / 发布示例）时，请显式加 --share。", file=sys.stderr)
        print("            用法见: python3 desensitize.py --help", file=sys.stderr)
        sys.exit(2)

    mf = "_desensitize_map.json"
    if "--manifest" in argv:
        mf = argv[argv.index("--manifest") + 1]
    manifest = _load_manifest(mf)

    if "--package" in argv:
        src_dir = argv[argv.index("--package") + 1]
        out_dir = argv[argv.index("--out-dir") + 1] if "--out-dir" in argv else \
            os.path.join(os.path.dirname(os.path.abspath(src_dir)), "_share_package")
        if not os.path.isdir(src_dir):
            print(f"FAIL: 源目录不存在: {src_dir}", file=sys.stderr)
            sys.exit(1)
        os.makedirs(out_dir, exist_ok=True)
        rc = make_share_package(src_dir, out_dir, manifest, mf)
        _save_manifest(mf, manifest)
        sys.exit(rc)

    # 单文件模式：<input> <output>
    pos = [a for a in argv if not a.startswith("--") and a != mf]
    if len(pos) < 2:
        print(__doc__)
        sys.exit(2)
    src, dst = pos[0], pos[1]
    if not os.path.isfile(src):
        print(f"FAIL: 输入文件不存在: {src}", file=sys.stderr)
        sys.exit(1)
    hits = {}
    masked = desensitize_text_file(src, dst, manifest, hits)
    _save_manifest(mf, manifest)
    print(f"脱敏完成: {src} → {dst}（{masked} 行含脱敏点；占位符 {len(manifest)} 种；命中 {sum(hits.values())} 处）")
    print(f"映射清单(只留本地): {mf}")
    print(f"提示: 本模式服务于分享场景；私有备份/还原请勿调用本脚本（v{VERSION} 起默认拒绝无 --share 调用）。")


if __name__ == "__main__":
    main()
