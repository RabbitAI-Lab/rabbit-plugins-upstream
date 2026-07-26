# hekouwang-typora-theme-skill

会勇禾口王 · **Typora 主题工程 Skill**。

维护「hekouwang」主题（复刻 Claude 桌面端阅读体验，深浅双版），并把一套主题工程方法
固化成可复用工具。

![screenshot](docs/screenshot.png)

## 它解决什么

做主题真正费时间的不是写 CSS，而是**一类不报错的失败**：改了 CSS 但 Typora 没变化、
字体没生效却照常渲染、配色凭直觉猜结果和参照对不上、主题菜单里多出个奇怪条目。
这些都不会抛错，只会让你在错误的基础上继续调。

所以这个 skill 的重点是三件事：

1. **CSS 由 `tokens.json` 生成**，不手写。构建时强制断言：0 个 `!important`、
   除根字号外 0 处 px 字号（后者会让 Typora 的字号调节失效，但页面看起来完全正常）。
2. **采样，不猜配色**。`sample_colors.py` 从参照截图取真实像素，还能反解叠加色的 alpha
   —— 三通道解出一致的那个才是真的。实测靠这个推翻过两次凭直觉的判断。
3. **验证要能分辨真假**。`verify_render.py` 永远带一个"不存在的字体"作 fallback 基准，
   任何字体量出来等于基准就说明它没生效。没有基准的宽度数字毫无意义。

## 用法

装进 `~/.claude/skills/` 后，直接对 Claude Code 说：

> 帮我把 Typora 主题的行高调紧一点
> 我的主题字体好像没生效，查一下
> 按这张截图的配色做一套主题

或手动：

```bash
python3 scripts/build.py       # tokens.json → 两个 CSS（含自检）
./scripts/install.sh           # 装进 Typora
python3 scripts/verify_render.py --css theme/hekouwang.css --fonts "Hekouwang Sans"
python3 scripts/sample_colors.py 参照.png --box 700,640,1700,700 --label 正文背景
```

⚠️ 改完 CSS 必须 **`Cmd+Q` 完全退出 Typora 再重开** —— 切换主题不会重新加载被修改的文件。

## 文档

| | |
|---|---|
| [SKILL.md](SKILL.md) | 入口与铁律 |
| [references/tokens.md](references/tokens.md) | 调参口径：改哪个值管什么 |
| [references/typora-spec.md](references/typora-spec.md) | 选择器地图、官方规范、五个静默坑 |
| [references/fonts.md](references/fonts.md) | 字体策略、授权红线、三级降级 |
| [references/workflow.md](references/workflow.md) | 做新主题 / 加变体 / 发布到主题库 |

## 相关

- 主题仓库（可直接下载安装）：https://github.com/huiyonghkw/hekouwang-typora-theme
- Typora 主题库提交：[typora/theme.typora.io#523](https://github.com/typora/theme.typora.io/pull/523)

## 授权

MIT，见 [LICENSE.txt](LICENSE.txt)（用 `.txt` 后缀是因为 SkillHub 的发布白名单不收无扩展名文件）。
随包的 Inter 字体采用 SIL OFL 1.1。
本 skill 不包含、不分发任何 Anthropic 专有字体。
