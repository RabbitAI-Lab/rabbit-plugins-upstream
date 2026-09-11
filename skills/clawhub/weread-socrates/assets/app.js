"use strict";
const $ = (id) => document.getElementById(id);
const providers = {
  zhipu: {
    name: "智谱 GLM",
    endpoint: "https://open.bigmodel.cn/api/paas/v4/chat/completions",
    model: "glm-4-flash",
  },
  deepseek: {
    name: "DeepSeek",
    endpoint: "https://api.deepseek.com/v1/chat/completions",
    model: "deepseek-chat",
  },
};
const state = {
  mode: "demo",
  book: null,
  highlights: [],
  selected: new Set(),
  memory: [],
  outline: "",
  history: [],
  round: 0,
  provider: localStorage.getItem("ai_provider") || "zhipu",
  key: localStorage.getItem("ai_key") || "",
};
function toast(text) {
  const n = $("toast");
  n.textContent = text;
  n.style.display = "block";
  clearTimeout(n.timer);
  n.timer = setTimeout(() => (n.style.display = "none"), 2600);
}
function clear(node) {
  while (node.firstChild) node.removeChild(node.firstChild);
}
function node(tag, text, cls) {
  const n = document.createElement(tag);
  if (text !== undefined) n.textContent = text;
  if (cls) n.className = cls;
  return n;
}
async function jsonFetch(url, options = {}) {
  const r = await fetch(url, options);
  const d = await r.json().catch(() => ({}));
  if (!r.ok) throw new Error(d.error || d.errmsg || `HTTP ${r.status}`);
  return d;
}
function consent(key, message) {
  if (sessionStorage.getItem(key) === "yes") return true;
  if (!confirm(message)) return false;
  sessionStorage.setItem(key, "yes");
  return true;
}
async function check() {
  try {
    const d = await jsonFetch("/api/status");
    state.mode = d.mode;
    $("status").textContent =
      `${d.mode === "demo" ? "Demo 模式（不外发）" : "在线模式"} · v${d.skillVersion} · ${d.host}:${d.port}`;
    loadMemory();
  } catch (e) {
    $("status").textContent = "无法连接本地服务：" + e.message;
  }
}
async function weread(api, params) {
  if (
    state.mode === "live" &&
    !consent(
      "consent_weread",
      "即将把搜索条件/书籍标识发送到微信读书，并读取相关书籍数据。是否同意本次浏览器会话使用微信读书在线服务？",
    )
  )
    throw new Error("你未同意连接微信读书");
  return jsonFetch("/api/weread", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ api_name: api, ...params }),
  });
}
async function search() {
  const keyword = $("searchInput").value.trim();
  if (!keyword) return;
  $("status").textContent = "正在搜索…";
  try {
    const d = await weread("/store/search", { keyword, count: 3 });
    const books = (d.results || []).flatMap((x) => x.books || []);
    if (!books.length) throw new Error("没有找到书籍");
    const b = books[0].bookInfo;
    state.book = {
      bookId: b.bookId,
      title: b.title,
      author: b.author || "",
      cover: b.cover || "",
    };
    const [info, chapters, marks] = await Promise.all([
      weread("/book/info", { bookId: b.bookId }),
      weread("/book/chapterinfo", { bookId: b.bookId }),
      weread("/book/bestbookmarks", {
        bookId: b.bookId,
        chapterUid: 0,
        synckey: 0,
      }),
    ]);
    state.book.intro = info.intro || "";
    state.book.chapters = chapters.chapters || [];
    renderBook();
    renderHighlights(
      (marks.items || []).map((x) => ({
        text: x.markText,
        chapter:
          (marks.chapters || []).find((c) => c.chapterUid === x.chapterUid)
            ?.title || "",
        meta: `${x.totalCount || 0} 人划线`,
      })),
    );
    await makeOutline();
  } catch (e) {
    $("status").textContent = "搜索失败：" + e.message;
  }
}
function renderBook() {
  const box = $("bookMeta");
  clear(box);
  const wrap = node("div", undefined, "book");
  if (state.book.cover) {
    const img = node("img");
    img.src = state.book.cover;
    img.alt = "封面";
    img.referrerPolicy = "no-referrer";
    wrap.append(img);
  }
  const info = node("div");
  info.append(
    node("strong", state.book.title),
    node("div", state.book.author, "muted"),
  );
  wrap.append(info);
  box.append(wrap);
  $("bookPanel").classList.remove("hidden");
}
function renderHighlights(items) {
  state.highlights = items.filter((x) => x.text);
  state.selected.clear();
  const box = $("highlights");
  clear(box);
  state.highlights.forEach((h, i) => {
    const n = node("div", h.text, "highlight");
    n.append(node("small", `\n${h.chapter || ""} ${h.meta || ""}`));
    n.onclick = () => {
      n.classList.toggle("selected");
      n.classList.contains("selected")
        ? state.selected.add(i)
        : state.selected.delete(i);
      $("startChat").disabled = !state.selected.size;
    };
    box.append(n);
  });
  $("startChat").disabled = true;
}
async function loadMine() {
  if (
    state.mode === "live" &&
    !consent(
      "consent_personal",
      "“我的划线”会读取你的微信读书个人划线和想法，并显示在本机页面。除非之后另行同意在线模型外发，这些个人数据不会发给模型供应商。是否继续？",
    )
  )
    return;
  try {
    const [b, r] = await Promise.all([
      weread("/book/bookmarklist", { bookId: state.book.bookId }),
      weread("/review/list/mine", {
        bookid: state.book.bookId,
        synckey: 0,
        count: 50,
      }),
    ]);
    const chapters = b.chapters || [];
    const items = (b.updated || [])
      .filter((x) => x.type === 1 && x.markText)
      .map((x) => ({
        text: x.markText,
        chapter:
          chapters.find((c) => c.chapterUid === x.chapterUid)?.title || "",
        meta: "我的划线",
      }));
    (r.reviews || []).forEach((x) => {
      const v = x.review || {};
      if (v.abstract)
        items.push({
          text: v.abstract,
          chapter: v.chapterName || "",
          meta: v.content ? `我的想法：${v.content}` : "我的想法",
        });
    });
    renderHighlights(items);
    if (!items.length) toast("没有可显示的个人划线");
  } catch (e) {
    toast("读取个人数据失败：" + e.message);
  }
}
function localOutline() {
  const cs = (state.book.chapters || [])
    .slice(0, 12)
    .map((c) => `  ${c.title}`)
    .join("\n");
  return `${state.book.title}\n  核心问题\n    如何检验自己的判断\n    如何把观点用于生活\n  章节路径\n${cs || "    智慧与无知\n    法律与良知\n    善的生活"}`;
}
async function makeOutline() {
  const context = `书名：${state.book.title}\n作者：${state.book.author}\n简介：${state.book.intro}\n章节：${(state.book.chapters || []).map((x) => x.title).join("；")}`;
  try {
    state.outline = state.key
      ? await llm([
          {
            role: "system",
            content:
              "输出纯文本缩进式导图，每行一个节点，只允许普通文字与空格缩进，不输出 HTML、SVG、Markdown 或代码。",
          },
          { role: "user", content: context },
        ])
      : localOutline();
  } catch (e) {
    state.outline = localOutline();
    toast("在线导图失败，已使用本地结构");
  }
  renderOutline();
}
function sanitizeOutline(text) {
  return String(text)
    .replace(/[<>]/g, "")
    .split(/\r?\n/)
    .slice(0, 120)
    .map((x) => x.slice(0, 120))
    .join("\n");
}
function renderOutline() {
  state.outline = sanitizeOutline(state.outline);
  const pre = node("pre", state.outline, "safe-outline");
  clear($("outline"));
  $("outline").append(pre);
}
async function llm(messages) {
  if (!state.key) return "";
  if (
    !consent(
      "consent_model",
      `将把当前书籍信息、所选原文和对话发送给 ${providers[state.provider].name}。可能包含你的个人划线、想法和回答。是否同意本次浏览器会话外发？`,
    )
  )
    throw new Error("你未同意向模型供应商外发数据");
  const p = providers[state.provider];
  const r = await fetch(p.endpoint, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
      Authorization: `Bearer ${state.key}`,
    },
    body: JSON.stringify({
      model: p.model,
      messages,
      temperature: 0.6,
      stream: false,
    }),
  });
  const d = await r.json().catch(() => ({}));
  if (!r.ok) throw new Error(d.error?.message || `模型 API ${r.status}`);
  return d.choices?.[0]?.message?.content || "";
}
const questions = [
  "这段文字中，哪个概念最需要先澄清？",
  "它与你的一次真实经历有什么联系？",
  "最有力的反对意见是什么？",
  "本周可以做出哪个可观察的改变？",
  "你现在保留的结论和未解问题分别是什么？",
];
async function startChat() {
  state.history = [];
  state.round = 0;
  $("chatPanel").classList.remove("hidden");
  clear($("chat"));
  await nextQuestion();
}
async function nextQuestion() {
  if (state.round >= 5) {
    toast("五轮对话已完成");
    return;
  }
  const selected = [...state.selected]
    .map((i) => state.highlights[i].text)
    .join("\n");
  let q = questions[state.round];
  if (state.key) {
    try {
      q = await llm([
        {
          role: "system",
          content:
            "你是中文苏格拉底式阅读教练。每轮只问一个具体、温和、有深度的问题。",
        },
        ...state.history,
        {
          role: "user",
          content: `原文：${selected}\n请进行第 ${state.round + 1}/5 轮提问。`,
        },
      ]);
    } catch (e) {
      toast(e.message);
      return;
    }
  }
  state.history.push({ role: "assistant", content: q });
  $("chat").append(node("div", `教练：${q}`, "msg ai"));
  state.round++;
  if (state.round >= 5) $("sendAnswer").disabled = true;
}
async function answer() {
  const text = $("answer").value.trim();
  if (!text) return;
  state.history.push({ role: "user", content: text });
  $("chat").append(node("div", `我：${text}`, "msg user"));
  $("answer").value = "";
  await nextQuestion();
}
async function loadMemory() {
  try {
    const d = await jsonFetch("/api/memory");
    state.memory = d.entries || [];
    renderMemory();
  } catch (e) {
    toast(e.message);
  }
}
async function saveMemory() {
  const content = $("memoryContent").value.trim();
  if (!content) return;
  await jsonFetch("/api/memory", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({
      type: $("memoryType").value,
      content,
      tags: $("memoryTags").value.split(/[,，]/),
      bookId: state.book?.bookId || "",
      bookTitle: state.book?.title || "未关联书籍",
      author: state.book?.author || "",
    }),
  });
  $("memoryContent").value = "";
  await loadMemory();
}
async function deleteOne(id) {
  await jsonFetch("/api/memory?id=" + encodeURIComponent(id), {
    method: "DELETE",
  });
  await loadMemory();
}
async function clearMemory() {
  if (!state.memory.length) return;
  const issued = await jsonFetch("/api/memory/delete-token", {
    method: "POST",
  });
  const typed = prompt(
    `批量删除不可恢复。请输入一次性确认 token（60 秒有效）：\n${issued.token}`,
  );
  if (typed !== issued.token) {
    toast("token 不匹配，未删除");
    return;
  }
  await jsonFetch("/api/memory", {
    method: "DELETE",
    headers: { "X-Confirm-Token": typed },
  });
  await loadMemory();
  toast("Reader Memory 已清空");
}
function renderMemory() {
  const box = $("memoryList");
  clear(box);
  const links = new Map();
  state.memory.forEach((e) => {
    const n = node("div", undefined, "memory");
    const del = node("button", "删除", "delete-one");
    del.onclick = () => deleteOne(e.id);
    n.append(
      del,
      node("small", `${e.type} · ${e.bookTitle || "未关联书籍"}`),
      node("div", e.content),
      node("div", (e.tags || []).map((t) => `#${t}`).join(" "), "tag"),
    );
    box.append(n);
    (e.tags || []).forEach((t) => {
      if (!links.has(t)) links.set(t, new Set());
      links.get(t).add(e.bookTitle || "未关联书籍");
    });
  });
  const cross = [...links]
    .filter(([, books]) => books.size > 1)
    .map(([tag, books]) => `#${tag}：${[...books].join(" ↔ ")}`);
  $("connections").textContent = cross.join("\n");
  $("connections").className = cross.length ? "connections" : "";
}
function download(text, name, type = "text/plain;charset=utf-8") {
  const u = URL.createObjectURL(new Blob([text], { type }));
  const a = node("a");
  a.href = u;
  a.download = name;
  a.click();
  setTimeout(() => URL.revokeObjectURL(u), 0);
}
function exportPng() {
  const lines = state.outline.split("\n");
  const c = node("canvas");
  c.width = 1200;
  c.height = Math.max(300, 80 + lines.length * 30);
  const x = c.getContext("2d");
  x.fillStyle = "#fff";
  x.fillRect(0, 0, c.width, c.height);
  x.fillStyle = "#292724";
  x.font = "22px sans-serif";
  lines.forEach((line, i) => x.fillText(line, 40, 55 + i * 30, 1120));
  c.toBlob((b) => {
    if (!b) return;
    const u = URL.createObjectURL(b);
    const a = node("a");
    a.href = u;
    a.download = `${state.book?.title || "读书"}-结构.png`;
    a.click();
    URL.revokeObjectURL(u);
  });
}
function exportNotes() {
  const selected = [...state.selected]
    .map((i) => `> ${state.highlights[i].text}`)
    .join("\n\n");
  const chat = state.history
    .map(
      (x) => `${x.role === "assistant" ? "**教练**" : "**我**"}：${x.content}`,
    )
    .join("\n\n");
  download(
    `# 《${state.book?.title || "阅读"}》伴读笔记\n\n${selected}\n\n## 对话\n\n${chat}\n\n> 仅供个人学习，请勿公开传播。`,
    "伴读笔记.md",
    "text/markdown;charset=utf-8",
  );
}
function bind() {
  $("searchBtn").onclick = search;
  $("searchInput").onkeydown = (e) => {
    if (e.key === "Enter") search();
  };
  $("hotBtn").onclick = search;
  $("mineBtn").onclick = loadMine;
  $("startChat").onclick = startChat;
  $("sendAnswer").onclick = answer;
  $("saveMemory").onclick = saveMemory;
  $("clearMemory").onclick = clearMemory;
  $("exportMemory").onclick = () =>
    download(
      JSON.stringify({ version: 1, entries: state.memory }, null, 2),
      "reader-memory.json",
      "application/json",
    );
  $("copyOutline").onclick = () =>
    navigator.clipboard.writeText(state.outline).then(() => toast("已复制"));
  $("exportPng").onclick = exportPng;
  $("exportNotes").onclick = exportNotes;
  $("settingsBtn").onclick = () => {
    $("provider").value = state.provider;
    $("apiKey").value = state.key;
    $("settings").showModal();
  };
  $("saveSettings").onclick = () => {
    state.provider = $("provider").value;
    state.key = $("apiKey").value.trim();
    localStorage.setItem("ai_provider", state.provider);
    if (state.key) localStorage.setItem("ai_key", state.key);
    else localStorage.removeItem("ai_key");
    sessionStorage.removeItem("consent_model");
    toast(state.key ? "在线模型已配置" : "已切换为本地 Demo");
  };
}
bind();
check();
