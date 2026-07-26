# Anki 导入与移动端指南（DramaLex）

## 桌面端导入（Anki / AnkiWeb）
1. 从 agent 拿到产出：`cards.tsv` + `media/` 文件夹（内含 `nnn_xxx.wav`）。
2. 打开 Anki → 文件 → 导入 → 选择 `cards.tsv`。
3. 导入选项中：
   - **字段分隔符**：选 `Tab`（本文件为 Tab 分隔）。
   - **允许在字段中使用 HTML**：勾选（背面含 `<br>`/`<b>` 等）。
   - 映射：栏 1→Front，栏 2→Back，栏 3→Audio（可选），栏 4→Tags。
   - 卡片模板：用默认 Basic（正面 Front / 背面 Back）。因 Front 为 `[sound:...]`，即"听音回想"，实现耳测。
4. 把 `media/` 里的 `.wav` 放入 Anki 媒体库：
   - 菜单 → 工具 → 管理媒体文件 → 可逐个添加；或直接将 `media/` 内容复制到 Anki 用户媒体目录（`~/Documents/Anki2/<用户>/collection.media/`）。
   - 也可直接用 `.apkg`（若 agent 生成了）：双击导入，音频已自动打包。

## 移动端（iOS / Android / Web）
- **AnkiMobile（iOS，付费）/ AnkiDroid（Android，免费）/ AnkiWeb**：登录同一账号 → 同步 → 牌组与音频自动下发。
- 手机上复习时，正面自动播放发音，背面显示拼写+释义+原句，天然支持"耳测"。
- 开启**每日提醒**：Anki 设置 → 通知/提醒 → 设定每日复习时间（跨 agent、不依赖某个 agent 在线）。

## 复习节奏（SM-2）
- Anki 默认按 SM-2 安排间隔（约 1/6/… 天）。每天 10–15 分钟即可维持。
- "不熟的词反复推送"由 SM-2 自动完成（答"生疏/忘记"会缩短间隔）。

## 常见坑
- 若导入后无声音：检查 `media/` 是否随 `cards.tsv` 一起放入媒体库，且文件名与 `[sound:...]` 一致。
- 若分隔错乱：确认导入时分隔符选了 Tab，而非逗号。
