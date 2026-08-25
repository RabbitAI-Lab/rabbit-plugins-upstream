#!/usr/bin/env node
// generate_gongwen_docx.js
// 将 Markdown 转换为符合 党政机关公文格式（GB/T 9704-2012）及通用公文排版规范的 Word 文档。
//
// 用法：
//   node generate_gongwen_docx.js input.md [output.docx]
//
// 生成后务必再运行后处理（补全 eastAsia 字体、双单位缩进、显式 Normal 样式）：
//   python fix_fonts.py output.docx
//
// 设计要点（全部来自多轮复审沉淀的公文规则）：
//   * 标题：二号方正小标宋简体、居中
//   * 层级（只定义四级）：一、黑体 / （一）楷体 / 1、仿宋 / （1）仿宋
//   * 正文：三号仿宋GB2312、首行缩进2字、两端对齐
//   * 第四层（1）属内容性分点：同正文缩进2字、两端对齐、段前段后0
//   * 标题（一~四级）一律顶格、段前段后0行
//   * 分点标点：同组（1）…（n），末项用“。”、其余用“；”
//   * 页码：页脚居中、无缩进、阿拉伯数字 Times New Roman
//   * 表格字体：默认四号（14pt）；首行水平+垂直居中、表头黑体
//   * 表格自动调整：「根据内容调整表格」（tblLayout=autofit，宽度 auto）
//   * 所有材料默认不加落款：所有模式（报告/标准）一律不输出落款，正文结束即结束
//   * 中文引号（" " ' ' 及全角形式）属高 ANSI 码位，Word 默认按 hAnsi（Times New Roman）渲染；
//     后处理 fix_fonts.py 将引号拆为独立 run 并强制用所在 run 的中文字体，确保引号用对应中文字体
//   * 中文之间 / 中文与标点之间多余空格自动清除：cleanup() 仅删“两侧均为 CJK 或中文标点”的空格，
//     保留“中文+拉丁/数字”之间的空格（如“标准 GB/T 9704”）；fix_fonts.py 再兜底一次
//
// 输入兼容三种写法：
//   A. 标准 Markdown 标题（# / ## / ### …），按深度自动编号；
//   B. 文字已带公文编号（一、 （一） 1、 （1）），含 **加粗** 伪装成标题的，
//      按编号直接定级——这样本技能可直接吃 IMA 导出的 md；
//   C. 「第X部分 / 第X章」分章型正式报告：自动进入“报告模式”——
//      · 第X部分 → 一、二、…八、 一级（黑体），每个 part 重置二级计数器；
//      · 其下的 ### 一、 / ### （一） / ### A类 统一降为 （一）（二）… 二级（楷体），
//        按 part 连续编号，杜绝“一、既是一级又是二级”的层级混乱；
//      · 报告模式**不渲染任何公文要素抬头**（主送/抄送/发文字号行）——标题后直接进入第一章节，无抬头；
//      · 报告模式与标准模式**默认均不加落款**（成文日期/呈报单位不输出），保持简洁；
//   IMA 外壳（空 #、开头“好的，根据…”、***、重复标题、（完整版））与 HTML 实体
//   （&#x7740; 等）均在生成阶段自动清理/解码，无需手工预处理。

const fs = require("fs");
const {
  Document, Packer, Paragraph, TextRun, Table, TableRow, TableCell,
  AlignmentType, BorderStyle, WidthType, ShadingType, VerticalAlign,
  Footer, PageNumber, TableLayoutType
} = require("docx");

// ====== 字体 / 字号 ======
const F_BODY  = "仿宋_GB2312";
const F_TITLE = "方正小标宋简体";
const F_H1    = "黑体";
const F_H2    = "楷体_GB2312";
const F_TABLE = "仿宋_GB2312";
const S_BODY  = 32;  // 三号 = 16pt
const S_TITLE = 44;  // 二号 = 22pt
const S_TABLE = 28;  // 四号 = 14pt（表格内字体默认四号）
const S_PAGE  = 28;  // 四号 = 14pt
const LINE    = 560; // 固定值 28 磅

const NOINDENT   = { firstLine: 0, firstLineChars: 0 };
const BODYINDENT = { firstLine: 640, firstLineChars: 200 };

// 阿拉伯数字 -> 中文数字（自动编号用；支持 1~99）
function cn(n) {
  const d = ["零", "一", "二", "三", "四", "五", "六", "七", "八", "九"];
  if (n <= 10) return n === 10 ? "十" : d[n];
  if (n < 20) return "十" + d[n % 10];
  if (n < 100) {
    const t = Math.floor(n / 10), u = n % 10;
    return d[t] + "十" + (u ? d[u] : "");
  }
  return String(n);
}

// ====== HTML 实体解码（IMA 导出常见 &#x7740; / &#29420; / &amp; 等）======
function decodeEntities(s) {
  return s
    .replace(/&#x([0-9a-fA-F]+);/g, (m, h) => { try { return String.fromCodePoint(parseInt(h, 16)); } catch (e) { return m; } })
    .replace(/&#(\d+);/g, (m, d) => { try { return String.fromCodePoint(parseInt(d, 10)); } catch (e) { return m; } })
    .replace(/&amp;/g, "&").replace(/&lt;/g, "<").replace(/&gt;/g, ">")
    .replace(/&quot;/g, '"').replace(/&nbsp;/g, " ");
}

// ====== 段落构造器 ======
function titleP(t) {
  return new Paragraph({
    alignment: AlignmentType.CENTER, indent: NOINDENT,
    spacing: { before: 240, after: 400, line: LINE, lineRule: "exact" },
    children: [ new TextRun({ text: cleanup(t), font: F_TITLE, size: S_TITLE }) ]
  });
}
function h1(t) { // 一、 黑体 首行缩进2字 段前段后0
  return new Paragraph({ indent: BODYINDENT, spacing: { before: 0, after: 0, line: LINE, lineRule: "exact" },
    children: [ new TextRun({ text: cleanup(t), font: F_H1, size: S_BODY }) ] });
}
function h2(t) { // （一） 楷体 首行缩进2字 段前段后0
  return new Paragraph({ indent: BODYINDENT, spacing: { before: 0, after: 0, line: LINE, lineRule: "exact" },
    children: [ new TextRun({ text: cleanup(t), font: F_H2, size: S_BODY }) ] });
}
function h3(t) { // 1、 仿宋 首行缩进2字 段前段后0
  return new Paragraph({ indent: BODYINDENT, spacing: { before: 0, after: 0, line: LINE, lineRule: "exact" },
    children: [ new TextRun({ text: cleanup(t), font: F_BODY, size: S_BODY }) ] });
}
function h4(t) { // （1） 分点：仿宋、同正文缩进2字、两端对齐、段前段后0
  return new Paragraph({ alignment: AlignmentType.JUSTIFIED, indent: BODYINDENT,
    spacing: { before: 0, after: 0, line: LINE, lineRule: "exact" },
    children: [ new TextRun({ text: cleanup(t), font: F_BODY, size: S_BODY }) ] });
}
function p(t) { // 正文：仿宋、缩进2字、两端对齐
  return new Paragraph({ alignment: AlignmentType.JUSTIFIED, indent: BODYINDENT,
    spacing: { after: 80, line: LINE, lineRule: "exact" },
    children: [ new TextRun({ text: cleanup(t), font: F_BODY, size: S_BODY }) ] });
}
// 主送机关：上行文三号黑体、顶格、无首行缩进
function zhusongP(t) {
  return new Paragraph({ indent: NOINDENT, spacing: { before: 0, after: 160, line: LINE, lineRule: "exact" },
    children: [ new TextRun({ text: cleanup(t), font: F_H1, size: S_BODY }) ] });
}
// 发文字号：仿宋、居中
function docNoP(t) {
  return new Paragraph({ alignment: AlignmentType.CENTER, indent: NOINDENT,
    spacing: { before: 0, after: 160, line: LINE, lineRule: "exact" },
    children: [ new TextRun({ text: cleanup(t), font: F_BODY, size: S_BODY }) ] });
}
// 落款：仿宋、右对齐、右空 N 字（rightChars 单位 1/100 字）
function signP(t, rightChars) {
  return new Paragraph({ alignment: AlignmentType.RIGHT,
    indent: { firstLine: 0, firstLineChars: 0, right: Math.round(rightChars / 100 * 320), rightChars },
    spacing: { before: 0, after: 0, line: LINE, lineRule: "exact" },
    children: [ new TextRun({ text: cleanup(t), font: F_BODY, size: S_BODY }) ] });
}

// 去掉行内 markdown 标记（** * ` 及链接），公文不强调
function inline(s) {
  return cleanup(
    s
      .replace(/\*\*(.+?)\*\*/g, "$1")
      .replace(/\*(.+?)\*/g, "$1")
      .replace(/`(.+?)`/g, "$1")
      .replace(/\[(.+?)\]\((.+?)\)/g, "$1")
      .replace(/\*/g, "")   // 兜底：清除任何不成对的残留星号（替换为空）
  );
}

// 去除中文（含中文标点）之间多余的空格：仅当空格两侧均为 CJK 字符或中文标点时才删除，
// 保留“中文 + 拉丁/数字”之间的空格（如“标准 GB/T 9704”“2026 年”），符合公文排版。
// CJK 范围：汉字 + 中文标点（，。、；：？！“”‘’（）【】《》·…— 等）+ 全角标点。
function cleanup(s) {
  if (typeof s !== "string") return s;
  const CJK = "[\u3400-\u4DBF\u4E00-\u9FFF\u3001-\u303F\uFF00-\uFFEF\u2018\u2019\u201C\u201D]";
  const WS = "[ \\t\\n\\r\\f\\v\u3000]+";
  return s.replace(new RegExp("(" + CJK + ")" + WS + "(" + CJK + ")", "g"), "$1$2");
}

// 去掉分点的既有编号前缀（统一重排为 （1）（2）…）
function stripPointPrefix(t) {
  return t.replace(/^[（(]?\s*\d+\s*[、）)]\s*/, "").trim();
}

// 判断一段“裸文本”属于哪种公文层级
function classify(t) {
  const s = inline(t).trim();
  if (/^[一二三四五六七八九十百]+、/.test(s)) return { kind: "h1", raw: s };
  if (/^（[一二三四五六七八九十]+）/.test(s)) return { kind: "h2", raw: s };
  if (/^[0-9]+、/.test(s)) return { kind: "h3", raw: s };
  if (/^（[0-9]+）/.test(s)) return { kind: "h4", raw: s };
  if (/^[0-9]+[）)]/.test(s)) return { kind: "h4", raw: s }; // 1） -> 分点
  return { kind: "body", raw: s };
}

// ====== 解析 Markdown ======
function parseBlocks(md) {
  const lines = md.split(/\r?\n/);
  const blocks = [];
  let i = 0;
  while (i < lines.length) {
    const raw = lines[i].replace(/\s+$/, "");
    if (raw.trim() === "") { i++; continue; }
    if (/^\s*\*{3,}\s*$/.test(raw)) { i++; continue; }              // 分隔线 ***
    if (/^\s*#\s*$/.test(raw)) { i++; continue; }                   // 空标题（IMA 外壳）
    if (raw.trim().startsWith("好的，根据我们")) { i++; continue; }  // IMA 对话外壳
    if (raw.trim() === "（完整版）" || raw.trim() === "**（完整版）**") { i++; continue; }

    // 公文要素（front-matter）：**主送：** / **日期：** / **呈报单位：** / **文件编号：** 等
    // 注意冒号可能位于加粗标记内部（**主送：**），故先去掉 ** 再匹配 key
    const bare = raw.replace(/\*\*/g, "");
    const fmm = bare.match(/^\s*(主送|抄送|呈报单位|日期|成文日期|文件编号|发文机关署名)[：:]\s*(.*)$/);
    if (fmm) { blocks.push({ type: "fm", key: fmm[1], value: fmm[2].trim() }); i++; continue; }

    // 表格
    if (raw.trim().startsWith("|") && i + 1 < lines.length &&
        /^\s*\|?[\s:|-]+[|]?\s*$/.test(lines[i + 1])) {
      const tbl = [raw];
      i++;
      tbl.push(lines[i]); i++; // 分隔行
      while (i < lines.length && lines[i].trim().startsWith("|")) { tbl.push(lines[i]); i++; }
      blocks.push({ type: "table", raw: tbl });
      continue;
    }

    // markdown 标题
    const hm = raw.match(/^(#{1,6})\s+(.*)$/);
    if (hm) {
      const level = hm[1].length;
      const text = hm[2].trim();
      const c = classify(text);
      if (c.kind !== "body") {
        blocks.push({ type: "heading", kind: c.kind, text: c.raw, auto: false, mdLevel: level });
      } else {
        const map = { 2: "h1", 3: "h2", 4: "h3", 5: "h4", 6: "h4" };
        blocks.push({ type: "heading", kind: map[level] || "h4", text, auto: true, mdLevel: level });
      }
      i++; continue;
    }

    // 列表：- * + 或 1. / 1、 / 1）
    const lm = raw.match(/^\s*[-*+]\s+(.*)$/);
    const om = raw.match(/^\s*\d+[.、)]\s+(.*)$/);
    if (lm || om) {
      const text = (lm ? lm[1] : om[1]).trim();
      const c = classify(text);
      if (c.kind === "body") {
        blocks.push({ type: "heading", kind: "h4", text: c.raw, auto: true, mdLevel: 99 });
      } else {
        blocks.push({ type: "heading", kind: c.kind, text: c.raw, auto: false, mdLevel: 99 });
      }
      i++; continue;
    }

    // 普通段落（合并连续非结构行）
    let buf = raw;
    i++;
    while (i < lines.length) {
      const nx = lines[i];
      if (nx.trim() === "") break;
      if (/^(#{1,6})\s/.test(nx)) break;
      if (/^\s*[-*+]\s/.test(nx)) break;
      if (/^\s*\d+[.、)]\s/.test(nx)) break;
      if (nx.trim().startsWith("|")) break;
      if (/^\s*\*{3,}\s*$/.test(nx)) break;
      buf += "\n" + nx; i++;
    }
    blocks.push({ type: "para", text: buf.trim() });
  }
  return blocks;
}

// ====== 组装段落 ======
function build(blocks, reportMode) {
  const children = [];
  let titleAdded = false, titleText = null;
  let c1 = 0, c2 = 0, c3 = 0;
  let pending = []; // 待输出的 分点 组
  let fmOrg = null, fmDate = null; // 落款要素

  function flushPending() {
    if (pending.length === 0) return;
    pending.forEach((txt, k) => {
      const t = txt.replace(/[；。、]+$/, "");
      const punct = k === pending.length - 1 ? "。" : "；";
      children.push(h4("（" + (k + 1) + "）" + t + punct));
    });
    pending = [];
  }

  for (const b of blocks) {
    if (b.type === "fm") {
      if (reportMode) {
        // 报告模式：标题后直接进入第一章节，无抬头、无发文字号行、无落款
        // （主送/抄送/文件编号/呈报单位/日期 一律不渲染）
        continue;
      }
      // 标准模式：抬头/发文字号渲染；落款要素收集后文末输出
      if (b.key === "呈报单位" || b.key === "发文机关署名") {
        fmOrg = b.value;
      } else if (b.key === "日期" || b.key === "成文日期") {
        fmDate = b.value;
      } else if (b.key === "主送" || b.key === "抄送") {
        flushPending();
        children.push(zhusongP((b.key === "主送" ? "主送：" : "抄送：") + b.value));
      } else if (b.key === "文件编号") {
        flushPending();
        children.push(docNoP(b.value));
      }
      continue;
    }
    if (b.type === "para") {
      const c = classify(b.text);
      if (c.kind === "body") { flushPending(); children.push(p(b.text)); }
      else if (c.kind === "h4") { pending.push(stripPointPrefix(c.raw)); }
      else { flushPending(); children.push(c.kind === "h1" ? h1(c.raw) : c.kind === "h2" ? h2(c.raw) : h3(c.raw)); }
      continue;
    }
    if (b.type === "table") { flushPending(); children.push(buildTable(b.raw)); continue; }
    if (b.type === "heading") {
      const k = b.kind;
      if (b.mdLevel === 1) { // markdown 一级标题 = 公文大标题（仅一个）
        flushPending();
        if (!titleAdded) { children.push(titleP(b.text)); titleAdded = true; titleText = b.text; }
        else if (b.text === titleText) { /* 跳过重复标题 */ }
        else { c1++; c2 = 0; c3 = 0; children.push(h1(cn(c1) + "、" + b.text)); }
        continue;
      }

      if (reportMode) {
        // ===== 报告模式：第X部分 → 一级；其下 ### → 二级；列表/分点 → （1）=====
        if (k === "h4") { pending.push(stripPointPrefix(b.text)); continue; }
        if (b.mdLevel === 2) {
          flushPending();
          c1++; c2 = 0; c3 = 0;
          const t = b.text.replace(/^第[一二三四五六七八九十百]+部分\s*/, "");
          children.push(h1(cn(c1) + "、" + t));
        } else {
          flushPending();
          c2++;
          // 去掉源稿里已有的 一、 / （一） 前缀，统一用 （一）（二）… 重排
          const t = b.text
            .replace(/^[一二三四五六七八九十百]+、/, "")
            .replace(/^（[一二三四五六七八九十]+）/, "");
          children.push(h2("（" + cn(c2) + "）" + t));
        }
        continue;
      }

      // ===== 标准模式（兼容 修改说明 等 clean 一、（一）1、（1）文档）=====
      if (k === "h1") {
        if (b.auto) { c1++; c2 = 0; c3 = 0; flushPending(); children.push(h1(cn(c1) + "、" + b.text)); }
        else { flushPending(); children.push(h1(b.text)); }
      } else if (k === "h2") {
        if (b.auto) { c2++; c3 = 0; flushPending(); children.push(h2("（" + cn(c2) + "）" + b.text)); }
        else { flushPending(); children.push(h2(b.text)); }
      } else if (k === "h3") {
        if (b.auto) { c3++; flushPending(); children.push(h3(c3 + "、" + b.text)); }
        else { flushPending(); children.push(h3(b.text)); }
      } else if (k === "h4") {
        pending.push(stripPointPrefix(b.text));
      }
    }
  }
  flushPending();

  // 文末落款：默认不输出。用户明确要求“落款也默认删除”——所有模式（报告/标准）均不加落款，
  // 保持公文正文结束即结束的简洁版式。如确需落款，可在源稿标注后放开下方开关：
  // if (fmOrg) children.push(signP(fmOrg, 200));
  // if (fmDate) children.push(signP(fmDate, 400));
  return children;
}

// ====== 表格 ======
function buildTable(raw) {
  const parseRow = (s) => s.replace(/^\s*\|/, "").replace(/\|\s*$/, "").split("|").map(x => inline(x).trim());
  const header = parseRow(raw[0]);
  const body = raw.slice(2).map(parseRow);
  const ncol = header.length;
  const total = 8845;               // A4 版心宽度（twips）
  const colw = Math.floor(total / ncol);
  const COLW = header.map(() => colw);
  const border = { style: BorderStyle.SINGLE, size: 4, color: "000000" };
  const borders = { top: border, bottom: border, left: border, right: border, insideHorizontal: border, insideVertical: border };
  function cell(text, opt = {}) {
    const { width, shade = false, head = false } = opt;
    const f = head ? F_H1 : F_TABLE;
    const al = head ? AlignmentType.CENTER : AlignmentType.LEFT;
    return new TableCell({
      borders,
      width: { size: width, type: WidthType.DXA },   // 首选列宽；autofit 布局下由内容重算
      shading: shade ? { fill: "D9D9D9", type: ShadingType.CLEAR } : undefined,
      margins: { top: 60, bottom: 60, left: 100, right: 100 },
      verticalAlign: VerticalAlign.CENTER,
      children: [ new Paragraph({
        indent: NOINDENT, alignment: al, spacing: { line: LINE, lineRule: "exact" },
        children: [ new TextRun({ text: cleanup(text), font: f, size: S_TABLE }) ]
      }) ]
    });
  }
  const rows = [ new TableRow({ children: header.map((h, idx) => cell(h, { width: COLW[idx], shade: true, head: true })) }) ];
  for (const r of body) rows.push(new TableRow({ children: r.map((c, idx) => cell(c, { width: COLW[idx] })) }));
  return new Table({
    width: { size: 0, type: WidthType.AUTO },
    columnWidths: COLW,            // 仅用于生成 w:tblGrid 网格结构，布局由 autofit 决定
    layout: TableLayoutType.AUTOFIT,
    rows
  });
}

// ====== 页脚（页码）======
const footer = new Footer({
  children: [ new Paragraph({
    alignment: AlignmentType.CENTER, indent: NOINDENT,
    spacing: { before: 0, after: 0, line: LINE, lineRule: "exact" },
    children: [ new TextRun({ font: "Times New Roman", size: S_PAGE, children: [ PageNumber.CURRENT ] }) ]
  }) ]
});

// ====== 主流程 ======
function main() {
  const input = process.argv[2];
  if (!input) { console.error("用法: node generate_gongwen_docx.js input.md [output.docx]"); process.exit(1); }
  let md = fs.readFileSync(input, "utf8");
  md = decodeEntities(md); // 自动解码 HTML 实体
  md = md.replace(/\*/g, ""); // 清除 markdown 星号（* 与 **），公文不保留任何 markdown 标记——批量替换为空

  // 报告模式：文档含「第X部分 / 第X章」分章标题
  // 注意：JS 的 \b 对 CJK 不生效（CJK 非 \w），改用 (?=\s|$) 作边界
  const reportMode = /^#{1,6}\s+第[一二三四五六七八九十百]+部分(?=\s|$)/m.test(md) ||
                    /^#{1,6}\s+第[一二三四五六七八九十百]+章(?=\s|$)/m.test(md);

  const children = build(parseBlocks(md), reportMode);
  const doc = new Document({
    sections: [{
      properties: { page: {
        size: { width: 11906, height: 16838 },                         // A4
        margin: { top: 2097, bottom: 1984, left: 1587, right: 1474 }  // 公文页边距
      }},
      footers: { default: footer },
      children
    }]
  });
  const out = process.argv[3] || input.replace(/\.md$/i, "_公文.docx");
  Packer.toBuffer(doc).then(buf => {
    fs.writeFileSync(out, buf);
    console.log("生成成功:", out, "字节:", buf.length, reportMode ? "（报告模式）" : "（标准模式）");
  });
}
main();
