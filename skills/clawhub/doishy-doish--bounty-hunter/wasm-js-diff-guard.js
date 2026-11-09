// wasm-js-diff-guard.js — cross-runtime hex parser differential (the #1315 family).
// WASM/Rust hex decoders and JS Buffer.from(hex) disagree on whitespace and
// malformed input. Flags the shape: the same node-supplied identifier flows
// into BOTH a normalizing/hash entrypoint (wasm `hex32`, `assetId*`, `trim()`)
// AND a raw JS decode (`Buffer.from(x, "hex")`, `new PublicKey(...)`) with no
// strict hex-shape validation (`/^[0-9a-fA-F]{64}$/`, `{64}`, length check)
// anywhere in the file. Either both must validate, or both must share one
// try/catch that rejects — anything else is a bypass seam.
// Returns rows: [{line, kind, detail}]. Empty = clean.
export function wasmJsDiffGuard(src, name = "<src>") {
  const rows = [];
  const text = String(src);
  const lines = text.split("\n");
  const hasStrictShape = /\/\^?\[0-9a-fA-F(\]\\)?\{64\}|\{64\}|length\s*(===|!==|==|!=|>|<)\s*64|BYTE_?LEN|byteLength\s*(===|!==)\s*32/.test(text);
  if (hasStrictShape) return rows;
  // Exemption: the fixed shape — normalizer call AND raw decode inside ONE
  // shared try block whose catch rejects (the Aug-27 scan.ts pattern). A
  // differential can't survive when every malformed shape funnels to REJECT.
  const spans = []; // {start, end} 0-based line spans of try blocks
  for (let i = 0; i < lines.length; i++) {
    if (!/\btry\s*\{/.test(lines[i])) continue;
    let depth = 0;
    for (let j = i; j < lines.length; j++) {
      depth += (lines[j].match(/\{/g) || []).length - (lines[j].match(/\}/g) || []).length;
      if (j > i && depth <= 0) { spans.push({ start: i, end: j }); break; }
    }
  }
  const normLines = [], decLines = [];
  lines.forEach((l, i) => {
    if (/(assetId\w*|verify\w*|hash\w*|digest\w*)\(\s*[A-Za-z_$][\w$]*\s*\)/.test(l) || /[A-Za-z_$][\w$]*\.trim\(\)/.test(l)) normLines.push(i);
    if (/Buffer\.from\(\s*[A-Za-z_$][\w$]*\s*,\s*["']hex["']\s*\)/.test(l) || /new\s+PublicKey\(\s*[A-Za-z_$][\w$]*\s*\)/.test(l)) decLines.push(i);
  });
  const sharedTry = normLines.some(n => decLines.some(d => spans.some(s => n >= s.start && n <= s.end && d >= s.start && d <= s.end)));
  if (sharedTry) return rows;
  const decodes = []; // {line, ident}
  const normalizers = new Set(); // idents passed to hash/wasm/trim fns
  lines.forEach((l, i) => {
    let m = l.match(/Buffer\.from\(\s*([A-Za-z_$][\w$]*)\s*,\s*["']hex["']\s*\)/);
    if (m) decodes.push({ line: i + 1, ident: m[1] });
    m = l.match(/new\s+PublicKey\(\s*([A-Za-z_$][\w$]*)\)/);
    if (m) decodes.push({ line: i + 1, ident: m[1], via: "PublicKey" });
    const n = l.match(/(assetId\w*|verify\w*|hash\w*|digest\w*)\(\s*([A-Za-z_$][\w$]*)\s*\)/) ||
      l.match(/([A-Za-z_$][\w$]*)\.trim\(\)/);
    if (n) normalizers.add(n[2] || n[1]);
  });
  for (const d of decodes) {
    if (normalizers.has(d.ident) && !hasStrictShape) {
      rows.push({ line: d.line, kind: "unvalidated-hex-across-boundary", detail: `"${d.ident}" feeds a normalizing hash fn and a raw JS decode with no strict 32-byte-hex shape check in ${name}` });
    }
  }
  // Standalone: trim() applied to hex that a sibling decode consumes raw.
  lines.forEach((l, i) => {
    const m = l.match(/([A-Za-z_$][\w$]*)\.trim\(\)/);
    if (m && new RegExp(`Buffer\\.from\\(\\s*${m[1]}\\s*,`).test(String(src)) && !hasStrictShape) {
      rows.push({ line: i + 1, kind: "trim-without-shape-check", detail: `"${m[1]}" is trimmed for one parser but raw-decoded by another; non-ASCII whitespace desyncs them` });
    }
  });
  return rows;
}
