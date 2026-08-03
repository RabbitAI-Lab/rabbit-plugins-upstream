# 通用增量组件库（所有公众号主题共用）

> 代码块、图片/GIF、小标签标题这三类组件所有主题共用，套用当前主题主色即可。
> 优先级：**先查主题库映射规则表**——该主题有等价语义组件就用主题库版本；主题库没有时才用本库。

## 使用规则

- 所有组件的 `{{主色}}` / `{{浅底色}}` / `{{下划线色}}` 占位符替换为当前主题的设计变量值
- 所有文字节点必须用 `<span leaf="">` 包裹
- 代码块每行一个 `<p style="margin:0">`，**绝不用 `white-space:pre`**
- 缩进用全角空格 `　`，行距靠 `line-height`

---

## 1. 代码块

### 1a. 深色代码块

```html
<section style="margin:20px 0;padding:16px 20px;background:#1e293b;border-radius:8px;overflow-x:auto;">
<p style="margin:0;line-height:1.6;font-size:14px;color:#e2e8f0;font-family:'SF Mono','Consolas','Monaco',monospace;"><span leaf=""><span leaf="" style="color:#93c5fd;">pip</span> install openai</span></p>
<p style="margin:0;line-height:1.6;font-size:14px;color:#e2e8f0;font-family:'SF Mono','Consolas','Monaco',monospace;"><span leaf=""><span leaf="" style="color:#6ee7b7;">from</span> openai <span leaf="" style="color:#6ee7b7;">import</span> OpenAI</span></p>
</section>
```

### 1b. 浅色代码块

```html
<section style="margin:20px 0;padding:16px 20px;background:#f1f5f9;border-radius:8px;border-left:3px solid {{主色}};overflow-x:auto;">
<p style="margin:0;line-height:1.6;font-size:14px;color:#334155;font-family:'SF Mono','Consolas','Monaco',monospace;"><span leaf="">npm create vite@latest my-app</span></p>
<p style="margin:0;line-height:1.6;font-size:14px;color:#334155;font-family:'SF Mono','Consolas','Monaco',monospace;"><span leaf="">cd my-app && npm install</span></p>
</section>
```

### 1c. 行内代码

```html
<span leaf="" style="background:#f1f5f9;color:#059669;padding:2px 6px;border-radius:4px;font-size:0.9em;font-family:'SF Mono','Consolas','Monaco',monospace;">`代码内容`</span>
```

行内代码示例（实际使用时去掉反引号，直接写代码内容）：

```html
<p style="margin:0;line-height:1.9;color:#374151;font-size:16px;"><span leaf="">运行命令 <span leaf="" style="background:#f1f5f9;color:#059669;padding:2px 6px;border-radius:4px;font-size:14px;font-family:'SF Mono','Consolas','Monaco',monospace;">npm run dev</span> 启动开发服务器</span></p>
```

---

## 2. 图片与 GIF

### 2a. 带说明的图片

```html
<section style="margin:24px 0;text-align:center;">
<img src="图片URL" style="max-width:100%;height:auto;display:block;margin:0 auto;border-radius:8px;" />
<p style="margin:8px 0 0;line-height:1.6;color:#9ca3af;font-size:13px;"><span leaf="">图片说明文字</span></p>
</section>
```

### 2b. GIF（带动图角标）

```html
<section style="margin:24px 0;text-align:center;position:relative;">
<img src="GIF的URL" style="max-width:100%;height:auto;display:block;margin:0 auto;border-radius:8px;" />
<section style="display:inline-block;margin-top:8px;padding:3px 10px;background:#f3f4f6;border-radius:12px;font-size:12px;color:#6b7280;"><span leaf="">GIF</span></section>
</section>
```

### 2c. 居中素材占位板块（待补素材用）

```html
<section style="margin:24px 0;padding:32px 20px;background:#f9fafb;border:2px dashed #d1d5db;border-radius:8px;text-align:center;">
<p style="margin:0;line-height:1.8;color:#9ca3af;font-size:14px;"><span leaf="">待补充素材</span></p>
<p style="margin:4px 0 0;line-height:1.6;color:#d1d5db;font-size:13px;"><span leaf="">在此处插入截图 / GIF / 成果图</span></p>
</section>
```

> 注意：此居中占位块使用 `dashed` 虚线框是被允许的——它是居中的素材占位组件，不是正文强调。正文强调用 3a-3e 的小标签。

---

## 3. 小标签与强调组件

### 3a. 左竖条小标题

```html
<section style="margin:24px 0;padding:8px 0 8px 14px;border-left:3px solid {{主色}};">
<p style="margin:0;line-height:1.6;font-size:17px;font-weight:bold;color:#1f2937;"><span leaf="">小标题文字</span></p>
</section>
```

### 3b. 药丸标签

```html
<section style="margin:16px 0 8px;">
<section style="display:inline-block;padding:4px 12px;background:{{浅底色}};border-radius:20px;">
<p style="margin:0;line-height:1.5;font-size:13px;color:{{主色}};font-weight:bold;"><span leaf="">标签文字</span></p>
</section>
</section>
```

### 3c. 步骤标签（Step Label）

```html
<section style="margin:20px 0;display:flex;align-items:center;">
<section style="flex-shrink:0;width:28px;height:28px;background:{{主色}};border-radius:50%;display:flex;align-items:center;justify-content:center;">
<p style="margin:0;line-height:1;font-size:14px;color:#ffffff;font-weight:bold;"><span leaf="">1</span></p>
</section>
<p style="margin:0 0 0 10px;line-height:1.6;font-size:16px;font-weight:bold;color:#1f2937;"><span leaf="">步骤标题</span></p>
</section>
```

### 3d. 左竖条金句/提示块

```html
<section style="margin:20px 0;padding:12px 16px;background:{{浅底色}};border-left:3px solid {{主色}};border-radius:0 6px 6px 0;">
<p style="margin:0;line-height:1.8;font-size:15px;color:#374151;"><span leaf="">这里是一段需要突出的金句或提示内容。</span></p>
</section>
```

### 3e. 居中金句

```html
<section style="margin:28px 0;padding:20px;text-align:center;">
<p style="margin:0;line-height:1.8;font-size:18px;font-weight:bold;color:#1f2937;letter-spacing:1px;"><span leaf="">核心金句内容</span></p>
<section style="margin:12px auto 0;width:40px;height:3px;background:{{主色}};border-radius:2px;"></section>
</section>
```

---

## 换色规则

通用库组件用到主色时，替换为当前主题的对应变量：

| 占位符 | emerald | graphite | sunset | ocean | rose |
|--------|---------|---------|--------|-------|------|
| `{{主色}}` | `#059669` | `#374151` | `#EA580C` | `#2563EB` | `#E11D48` |
| `{{浅底色}}` | `#ecfdf5` | `#f3f4f6` | `#FFF7ED` | `#EFF6FF` | `#FFF1F2` |
| `{{下划线色}}` | `#6ee7b7` | `#9ca3af` | `#FB923C` | `#93C5FD` | `#FB7185` |
