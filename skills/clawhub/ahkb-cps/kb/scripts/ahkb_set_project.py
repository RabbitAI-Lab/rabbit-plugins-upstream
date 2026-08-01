#!/usr/bin/env python3
"""
ahkb_set_project.py — AHKB 知识库参数设置 v0.1.0

图形界面版本，调整知识元和资源的链接权重等参数。
所有权重保存到 project_settings.json。
"""
import os, sys, json, random
sys.stdout.reconfigure(encoding='utf-8') if hasattr(sys.stdout, 'reconfigure') else None
from pathlib import Path
from tkinter import *
from tkinter import ttk, messagebox

# ─── 路径 ───
VAULT = None
SETTINGS_FILE = None


def find_workspace():
    """自动检测工作空间（Vault）路径。"""
    cwd = Path.cwd().resolve()
    for parent in [cwd] + list(cwd.parents):
        if (parent / "知识元").exists():
            return parent
    return None


def resolve_vault(args_workspace=None):
    """确定工作空间路径：优先 --workspace，其次自动检测，最后报错退出。"""
    global VAULT, SETTINGS_FILE
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
    SETTINGS_FILE = VAULT / "系统设置" / "project_settings.json"

# ─── 参数定义 ───
# (key, 显示名, 说明, 默认值)
GROUP_PARAMS = [
    ("cGranularity",  "知识元颗粒度",  "值大→单个知识元更粗大、总数少",      0.5),
    ("cTextAmount",   "知识元详细程度",  "值大→各个知识元内容更详细、文字多",      0.5),
]

GROUP_WEIGHTS = [
    ("cContext",      "上下文描述相关性", "值大→上下文内容匹配对建立链接影响增大", 0.5),
    ("cTags",         "关键词标签相关性", "值大→关键词标签匹配对建立链接影响增大",    0.5),
    ("cStars",        "待链接资源重要性", "值大→资源的星星个数对建立链接影响增大",  0.5),
    ("cEdited",       "用户手动编辑过否", "值大→用户是否编辑过对建立链接影响增大",      0.5),
    ("cLinksDensity", "平均链接数量",     "值大→各个知识元上的链接数量总体增大",  0.5),
    ("cLinksNum",     "链接数量上限",     "值大→单个知识元上的链接数量上限增大",  0.5),
]

ALL_PARAMS = GROUP_PARAMS + GROUP_WEIGHTS

# ─── 字号 ───
FONT = "微软雅黑"


class SettingsApp:
    """AHKB 参数设置 GUI"""

    def __init__(self):
        self.root = Tk()
        self.root.title("AHKB 知识库参数设置")
        self.root.lift()
        self.root.focus_force()
        self.root.after(100, lambda: [self.root.lift(), self.root.focus_force()])
        # 窗口尺寸：高度不超过屏幕高度-60（给任务栏留空间）
        sw = self.root.winfo_screenwidth()
        sh = self.root.winfo_screenheight()
        w, h = 820, min(920, sh - 60)
        x = (sw - w) // 2 + random.randint(-40, 40)
        y = max(0, (sh - h) // 2 + random.randint(-40, 40))
        self.root.geometry(f"{w}x{h}+{x}+{y}")
        self.root.configure(bg='#1e1e1e')
        self.root.resizable(False, True)

        # ─── Canvas + Scrollbar 使内容在屏幕较小时可滚动 ───
        self.canvas = Canvas(self.root, bg='#1e1e1e', highlightthickness=0)
        self.scrollbar = Scrollbar(self.root, orient=VERTICAL, command=self.canvas.yview)
        self.canvas.configure(yscrollcommand=self.scrollbar.set)

        self.content_frame = Frame(self.canvas, bg='#1e1e1e')
        self._canvas_window = self.canvas.create_window(
            (0, 0), window=self.content_frame, anchor='nw'
        )

        # Canvas 尺寸变化时同步内部 frame 宽度
        self.canvas.bind("<Configure>", self._on_canvas_configure)
        # 内部 frame 尺寸变化时更新滚动区域
        self.content_frame.bind("<Configure>", self._on_frame_configure)
        # 鼠标滚轮支持（进入Canvas时绑定，离开时解绑，避免干扰其他控件）
        self.canvas.bind("<Enter>", self._bind_mousewheel)
        self.canvas.bind("<Leave>", self._unbind_mousewheel)

        self.canvas.pack(side=LEFT, fill=BOTH, expand=True)
        self.scrollbar.pack(side=RIGHT, fill=Y)

        self.weights = self._load_weights()
        self.sliders = {}
        self.val_labels = {}
        self.dirty = False  # 是否有未保存的修改

        self.root.protocol("WM_DELETE_WINDOW", self._on_close)
        self._build_ui()
        self.root.mainloop()

    # ─── 工具 ───

    def _load_weights(self):
        defaults = {key: 0.5 for key, _, _, _ in ALL_PARAMS}
        if SETTINGS_FILE is not None and SETTINGS_FILE.exists():
            try:
                data = json.loads(SETTINGS_FILE.read_text(encoding="utf-8"))
                for k in defaults:
                    if k in data.get("weights", {}):
                        defaults[k] = float(data["weights"][k])
            except Exception:
                pass
        return defaults

    def _save_weights(self):
        SETTINGS_FILE.parent.mkdir(parents=True, exist_ok=True)
        # 保留已有字段（如 kb_name），只更新 weights
        existing = {}
        if SETTINGS_FILE.exists():
            try:
                existing = json.loads(SETTINGS_FILE.read_text(encoding="utf-8"))
            except Exception:
                pass
        existing["weights"] = dict(self.weights)
        SETTINGS_FILE.write_text(
            json.dumps(existing, ensure_ascii=False, indent=2), encoding="utf-8"
        )

    # ─── 滚动支持 ───

    def _on_canvas_configure(self, event):
        """Canvas 尺寸变化时，保持内部 frame 宽度与 Canvas 一致。"""
        self.canvas.itemconfig(self._canvas_window, width=event.width)

    def _on_frame_configure(self, event):
        """内部 frame 尺寸变化时，更新 Canvas 的 scrollregion。"""
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))

    def _bind_mousewheel(self, event):
        """鼠标进入 Canvas 区域时绑定滚轮事件。"""
        self.canvas.bind_all("<MouseWheel>", self._on_mousewheel)

    def _unbind_mousewheel(self, event):
        """鼠标离开 Canvas 区域时解绑滚轮事件。"""
        self.canvas.unbind_all("<MouseWheel>")

    def _on_mousewheel(self, event):
        """处理鼠标滚轮滚动。"""
        self.canvas.yview_scroll(int(-1 * (event.delta / 120)), "units")

    # ─── 界面 ───

    def _make_label(self, parent, text, **kw):
        defaults = {"bg": '#1e1e1e', "fg": '#f0f0f0', "font": (FONT, 11)}
        defaults.update(kw)
        return Label(parent, text=text, **defaults)

    def _make_frame(self, parent, **kw):
        defaults = {"bg": '#2d2d2d', "relief": FLAT, "bd": 0}
        defaults.update(kw)
        return Frame(parent, **defaults)

    def _update_score_summary(self, info_label):
        cw = self.weights.get("cContext", 0.5)
        tw = self.weights.get("cTags", 0.5)
        sw = self.weights.get("cStars", 0.5)
        ew = self.weights.get("cEdited", 0.5)
        max_total = 212
        current_max = 100 * cw + 100 * tw + 10 * sw + 2 * ew
        text = (
            "上下文描述相关性：最高100分 × 权重\n"
            "关键词标签相关性：最高100分 × 权重\n"
            "待链接资源重要性：每颗星★2分 × 权重\n"
            "用户手动编辑过否：编辑过得2分 × 权重\n"
            f"\n总分最高（所有权重=1时）：{max_total}分\n"
            f"当前加权总分最高：{current_max:.0f}分\n"
            "\n最终得分 = 各项实际分数 × 权重 之和\n"
            "得分超过分数线即建立链接"
        )
        info_label.config(text=text)

    def _build_scale_row(self, parent, row, key, display_name, desc, default):
        self._make_label(parent, text=display_name,
                         font=(FONT, 11, "bold"),
                         anchor=W, justify=LEFT
                         ).grid(row=row, column=0, sticky=W, padx=(12, 5), pady=(8, 0))

        self._make_label(parent, text=desc,
                         font=(FONT, 10), fg='#b1b1b1',
                         anchor=W
                         ).grid(row=row+1, column=0, sticky=W, padx=(12, 5), pady=(0, 2))

        scale = Scale(parent, from_=0.0, to=1.0, resolution=0.1,
                      orient=HORIZONTAL, length=400,
                      bg='#3c3c3c', fg='#f0f0f0', troughcolor='#555555',
                      activebackground='#0e639c',
                      highlightthickness=0, bd=0)
        scale.set(self.weights.get(key, default))
        scale.grid(row=row, column=1, rowspan=2, sticky=EW, padx=(5, 5), pady=(8, 2))
        self.sliders[key] = scale

        val_label = Label(parent,
                          bg='#2d2d2d', fg='#4ec9b0', font=("Consolas", 14, "bold"),
                          width=4, anchor=E)
        val_label.config(text=f"{self.weights.get(key, default):.1f}")
        val_label.grid(row=row, column=2, rowspan=2, sticky=E, padx=(0, 12), pady=(8, 2))
        self.val_labels[key] = val_label

    def _build_ui(self):
        root = self.content_frame

        # ═══════ 标题 ═══════
        title_frame = Frame(root, bg='#1e1e1e')
        title_frame.pack(fill=X, padx=20, pady=(20, 8))

        Label(title_frame, text="AHKB 知识库参数设置",
              font=(FONT, 18, "bold"),
              bg='#1e1e1e', fg='#4ec9b0', anchor=W).pack(anchor=W)

        Label(title_frame,
              text="设置知识元如何抽取？如何链接资源（图片、音视频等）？所有参数均以【0~1的权重】的形式设置。",
              font=(FONT, 11),
              bg='#1e1e1e', fg='#b1b1b1', anchor=W).pack(anchor=W, pady=(4, 0))

        # ═══════ 总体参数设置 ═══════
        sep1 = Frame(root, bg='#3c3c3c', height=1)
        sep1.pack(fill=X, padx=20, pady=(10, 6))

        self._make_label(root, text="━━━ 知识元生成参数 ━━━",
                         font=(FONT, 12, "bold"), fg='#569cd6').pack(anchor=W, padx=20, pady=(4, 4))

        frame1 = self._make_frame(root)
        frame1.pack(fill=X, padx=20, pady=(0, 6))
        frame1.columnconfigure(1, weight=1)

        for i, (key, name, desc, default) in enumerate(GROUP_PARAMS):
            self._build_scale_row(frame1, i * 2, key, name, desc, default)

        # ═══════ 链接权重设置 ═══════
        sep2 = Frame(root, bg='#3c3c3c', height=1)
        sep2.pack(fill=X, padx=20, pady=(10, 6))

        self._make_label(root, text="━━━ 知识元与资源（图片、音视频等）链接参数 ━━━",
                         font=(FONT, 12, "bold"), fg='#569cd6').pack(anchor=W, padx=20, pady=(4, 4))

        frame2 = self._make_frame(root)
        frame2.pack(fill=X, padx=20, pady=(0, 6))
        frame2.columnconfigure(1, weight=1)

        for i, (key, name, desc, default) in enumerate(GROUP_WEIGHTS):
            self._build_scale_row(frame2, i * 2, key, name, desc, default)

        # 绑定权重滑块变化 → 更新评分说明
        def _bind_weight_sliders():
            for key in list(self.sliders.keys()):
                if key not in self.sliders:
                    continue
                s = self.sliders[key]
                def make_cmd(k):
                    return lambda v: self._on_weight_change(v, k)
                s.config(command=make_cmd(key))

        # ═══════ 底部：评分说明(左) + 按钮(右) ═══════
        bottom = Frame(root, bg='#1e1e1e')
        bottom.pack(fill=X, padx=20, pady=(6, 12))

        # ── 左右各占一半（用水平容器）──
        mid_row = Frame(bottom, bg='#1e1e1e')
        mid_row.pack(fill=X)
        mid_row.columnconfigure(0, weight=1)
        mid_row.columnconfigure(1, weight=1)

        # ── 左半：加权评分说明 ──
        left_half = Frame(mid_row, bg='#1e1e1e')
        left_half.grid(row=0, column=0, sticky=NSEW, padx=(0, 5))
        left_half.columnconfigure(0, weight=1)
        left_half.rowconfigure(0, weight=1)

        info_frame = self._make_frame(left_half)
        info_frame.grid(row=0, column=0, sticky=NSEW)

        Label(info_frame, text="加权评分说明",
              font=("Consolas", 13, "bold"),
              bg='#2d2d2d', fg='#e5e5e5', anchor=W, justify=LEFT,
              padx=10).pack(fill=X, pady=(8, 2))

        self.info_label = Label(info_frame,
                                font=("Consolas", 10),
                                bg='#2d2d2d', fg='#b1b1b1', anchor=W, justify=LEFT,
                                padx=10)
        self.info_label.pack(fill=X, pady=(0, 8))
        self._update_score_summary(self.info_label)
        _bind_weight_sliders()

        # ── 右半：注意 + 按钮 ──
        right_half = Frame(mid_row, bg='#1e1e1e')
        right_half.grid(row=0, column=1, sticky=NSEW, padx=(5, 0))

        Label(right_half, text="⚠ 注意",
              font=(FONT, 13, "bold"),
              bg='#1e1e1e', fg='#dcdcaa', anchor=W, justify=LEFT
              ).pack(fill=X, pady=(0, 2))

        Label(right_half, text='(1)修改后的知识元生成参数仅对后续生成知识元有效。若要对整个知识库生效，需运行"完全重建知识库"或"批量更新知识库"。\n(2)修改后的链接参数仅对后续生成链接有效。若要对整个知识库生效，需运行"自动整理知识库并更新知识链"。',
              font=(FONT, 11),
              bg='#1e1e1e', fg='#dcdcaa', anchor=NW, justify=LEFT,
              wraplength=480
              ).pack(fill=X, pady=(0, 4))

        # ── 状态栏（带边框） ──
        status_box = Frame(right_half, bg='#3c3c3c', bd=1, relief=SOLID)
        status_box.pack(fill=X, pady=(0, 6))

        self.status_var = StringVar(value="未修改")
        Label(status_box, text="当前状态：",
              font=(FONT, 12, 'bold'), fg='#569cd6',
              bg='#3c3c3c', anchor=W, justify=LEFT,
              padx=6, pady=4
              ).pack(side=LEFT)

        self.status_label = Label(status_box, textvariable=self.status_var,
              font=(FONT, 12),
              bg='#3c3c3c', fg='#b1b1b1', anchor=W, justify=LEFT,
              padx=6, pady=4)
        self.status_label.pack(side=LEFT)

        btn_row = Frame(right_half, bg='#1e1e1e')
        btn_row.pack(fill=X)

        self.btn_save = Button(btn_row, text="💾 保存设置",
                               font=(FONT, 11, "bold"),
                               bg='#0e639c', fg='white',
                               activebackground='#1177bb',
                               relief=FLAT, padx=20, pady=6,
                               state=DISABLED,
                               command=self._on_save)
        self.btn_save.pack(side=LEFT, fill=X, expand=True, padx=(0, 3))

        btn_close = Button(btn_row, text="关闭",
                           font=(FONT, 11),
                           bg='#3c3c3c', fg='#f0f0f0', activebackground='#555555',
                           relief=FLAT, padx=20, pady=6,
                           command=self._on_close)
        btn_close.pack(side=LEFT, fill=X, expand=True, padx=(3, 0))

    def _on_weight_change(self, val, key):
        v = round(float(val), 1)
        self.weights[key] = v
        if key in self.val_labels:
            self.val_labels[key].config(text=f"{v:.1f}")
        self._update_score_summary(self.info_label)
        self.status_var.set("参数已改变，尚未保存")
        self.status_label.config(fg='#f44336')
        self.dirty = True
        self.btn_save.config(state=NORMAL)

    def _on_close(self):
        """关闭时检查未保存的修改。"""
        if self.dirty:
            if messagebox.askyesno("未保存的修改",
                                   "参数已改变但尚未保存，确定关闭吗？",
                                   icon='warning'):
                self.root.destroy()
        else:
            self.root.destroy()

    def _on_save(self):
        for key in self.sliders:
            self.weights[key] = round(self.sliders[key].get(), 2)
        self._save_weights()
        self.status_var.set("已保存，下次重建知识库或更新知识链时生效")
        self.status_label.config(fg='#f44336')
        self.dirty = False
        self.btn_save.config(state=DISABLED)


if __name__ == "__main__":
    try:
        ws_arg = None
        if "--workspace" in sys.argv:
            idx = sys.argv.index("--workspace")
            if idx + 1 < len(sys.argv):
                ws_arg = sys.argv[idx + 1]
        resolve_vault(ws_arg)
        print(f"\n📂 知识库路径: {VAULT}")
        print("⚙  正在启动参数设置界面...\n")
        SettingsApp()
        print("✅ 参数设置已完成。\n")
    except ImportError as e:
        print(f"错误：缺少库 {e}")
        sys.exit(1)
