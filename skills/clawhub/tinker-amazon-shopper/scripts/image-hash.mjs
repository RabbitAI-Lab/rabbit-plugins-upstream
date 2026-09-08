// image-hash.mjs — perceptual hashing (dHash) for copycat detection.
//
// Amazon pool-chemical listings are full of copycats: the same physical
// product relabelled by different sellers, often a cent or two apart. Their
// product photos are usually IDENTICAL (same manufacturer press shot). A
// perceptual hash clusters those near-duplicate images cheaply — no ML, no
// paid API — so the ranker can collapse a cluster to its cheapest member.
//
// dHash (difference hash): resize to 9x8 grayscale, emit 1 bit per adjacent
// horizontal pixel pair (left > right). 64-bit hash. Robust to rescaling,
// compression, minor color shifts. Compared via Hamming distance:
//   0       → byte-identical render
//   1-10    → almost certainly the same image (copycat)
//   11-20   → similar layout, maybe same product family
//   20+     → different image
//
// Decoding uses the ImageMagick `convert` CLI (system dep, like the browser
// relay uses Chrome). Zero npm dependencies.

import { spawn } from "node:child_process";

const DEFAULT_CONVERT = process.env.AMAZON_SHOPPER_CONVERT_CMD || "convert";

// Pipe an image buffer through ImageMagick → 9x8 grayscale raw bytes (72 bytes).
function convertToGrayRaw(buf, convertCmd = DEFAULT_CONVERT) {
  return new Promise((resolve, reject) => {
    const child = spawn(convertCmd, ["-", "-resize", "9x8!", "-colorspace", "Gray", "-depth", "8", "gray:-"], {
      stdio: ["pipe", "pipe", "pipe"],
    });
    const chunks = [];
    let err = "";
    child.stdout.on("data", (d) => chunks.push(d));
    child.stderr.on("data", (d) => (err += d.toString()));
    child.on("error", reject);
    child.on("close", (code) => {
      if (code !== 0) return reject(new Error(`${convertCmd} exited ${code}: ${err.slice(0, 200)}`));
      resolve(Buffer.concat(chunks));
    });
    child.stdin.on("error", () => {}); // ignore EPIPE if convert bails early
    child.stdin.write(buf);
    child.stdin.end();
  });
}

// Compute dHash from a 72-byte (9x8) grayscale buffer.
export function dhashFromGrayRaw(raw) {
  if (!raw || raw.length < 72) {
    throw new Error(`expected >=72 grayscale bytes, got ${raw ? raw.length : 0}`);
  }
  let hash = 0n;
  let bit = 0n;
  for (let row = 0; row < 8; row++) {
    for (let col = 0; col < 8; col++) {
      if (raw[row * 9 + col] > raw[row * 9 + col + 1]) hash |= 1n << bit;
      bit++;
    }
  }
  return hash.toString(16).padStart(16, "0");
}

export async function dhashFromBuffer(buf, { convertCmd = DEFAULT_CONVERT } = {}) {
  const raw = await convertToGrayRaw(buf, convertCmd);
  return dhashFromGrayRaw(raw);
}

export async function downloadImage(url, { _fetch = globalThis.fetch, timeoutMs = 10000 } = {}) {
  const ctrl = new AbortController();
  const t = setTimeout(() => ctrl.abort(), timeoutMs);
  try {
    const res = await _fetch(url, { signal: ctrl.signal });
    if (!res.ok) throw new Error(`image fetch HTTP ${res.status}`);
    return Buffer.from(await res.arrayBuffer());
  } finally {
    clearTimeout(t);
  }
}

export function hammingDistance(hexA, hexB) {
  let x = BigInt("0x" + hexA) ^ BigInt("0x" + hexB);
  let count = 0;
  while (x) {
    count += Number(x & 1n);
    x >>= 1n;
  }
  return count;
}

// Hash every product's image (best-effort — failures leave image_hash null).
// Concurrency-capped; never throws (a copycat-detection failure must not break
// the whole search).
export async function hashProductImages(products, { concurrency = 4, _fetch = globalThis.fetch, convertCmd = DEFAULT_CONVERT, logger = null } = {}) {
  const queue = products.filter((p) => p.image_url);
  const work = [...queue];
  async function worker() {
    while (work.length) {
      const p = work.shift();
      try {
        const buf = await downloadImage(p.image_url, { _fetch });
        p.image_hash = await dhashFromBuffer(buf, { convertCmd });
      } catch (e) {
        p.image_hash = null;
        if (logger) logger(p, "image-hash", "error", p.image_url, e.message);
      }
    }
  }
  await Promise.all(Array.from({ length: Math.min(concurrency, queue.length) || 1 }, () => worker()));
  return products;
}

// Cluster products whose images are near-duplicates (Hamming <= threshold).
// Greedy single-link clustering — fine for the ~50-item scale here. Products
// without a hash each form their own singleton cluster.
// Returns: array of clusters, each an array of products. Each product is
// annotated with `cluster_id` and `cluster_size`.
export function clusterByImageHash(products, { threshold = 8 } = {}) {
  const clusters = [];
  for (const p of products) {
    if (!p.image_hash) {
      clusters.push([p]);
      continue;
    }
    let placed = false;
    for (const c of clusters) {
      const rep = c.find((x) => x.image_hash);
      if (rep && hammingDistance(rep.image_hash, p.image_hash) <= threshold) {
        c.push(p);
        placed = true;
        break;
      }
    }
    if (!placed) clusters.push([p]);
  }
  clusters.forEach((c, idx) => {
    for (const p of c) {
      p.cluster_id = idx;
      p.cluster_size = c.length;
    }
  });
  return clusters;
}

// Within each cluster, mark the cheapest as the representative. Returns the
// list of representatives (one per cluster) + annotates non-cheapest members
// with `cheaper_alternative_asin` pointing at the winner. This is the core
// "skip the copycat that's a cent more" value move.
export function pickCheapestPerCluster(clusters) {
  const reps = [];
  for (const c of clusters) {
    const priced = c.filter((p) => typeof p.current_price_eur === "number");
    const pool = priced.length ? priced : c;
    const cheapest = pool.reduce((best, p) => {
      if (best == null) return p;
      const bp = best.current_price_eur ?? Infinity;
      const pp = p.current_price_eur ?? Infinity;
      return pp < bp ? p : best;
    }, null);
    for (const p of c) {
      if (p !== cheapest && cheapest) p.cheaper_alternative_asin = cheapest.asin;
    }
    if (cheapest) {
      cheapest.cluster_member_count = c.length;
      reps.push(cheapest);
    }
  }
  return reps;
}
