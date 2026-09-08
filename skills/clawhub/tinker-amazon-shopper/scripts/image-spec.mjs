// image-spec.mjs — extract product spec from the product IMAGE when title +
// description don't carry it. Amazon pool-chemical packshots routinely print
// the concentration ("15%"), volume ("20 L"), net weight ("25 kg"), and
// dimensions right on the label — data the text fields often omit.
//
// Pipeline: download the image to a temp file → vision LLM reads the label →
// parse the same spec shape title-spec.mjs / research.mjs use. Wired as a
// research-ladder step for low-confidence products only (vision calls cost
// tokens, so it's gated, not blanket).

import { writeFile, unlink, mkdtemp } from "node:fs/promises";
import { tmpdir } from "node:os";
import { join } from "node:path";
import { callLLMVision } from "./llm.mjs";

const VISION_PROMPT = `\
You are reading an Amazon product photo of a pool/spa chemical. Extract ONLY
what is VISIBLE printed on the packaging label — do not guess from the product
name. Look for: net volume (L), net weight (kg), concentration (%), active
ingredient, and physical dimensions if shown.

Return ONLY this JSON:
{
  "package_size_l": <number or null>,
  "package_size_kg": <number or null>,
  "concentration_pct": <number 0-100 or null>,
  "active_ingredient": "<canonical English name or null>",
  "form": "<liquid|granular|null>",
  "dimensions_cm": "<e.g. 30x20x15 or null>",
  "confidence": <0..1 — how clearly the label states these>
}

If the label is not legible or shows none of these, set confidence < 0.3.`;

async function downloadImage(url, _fetch) {
  const res = await _fetch(url);
  if (!res.ok) throw new Error(`image download failed: HTTP ${res.status}`);
  const buf = Buffer.from(await res.arrayBuffer());
  const dir = await mkdtemp(join(tmpdir(), "ashop-img-"));
  // Keep the extension Amazon used (jpg/png) so the vision tool sniffs it right.
  const ext = (url.match(/\.(jpe?g|png|webp)(?:[?#]|$)/i)?.[1] || "jpg").toLowerCase();
  const path = join(dir, `product.${ext}`);
  await writeFile(path, buf);
  return path;
}

// analyzeProductImage — returns a spec object (same fields as title-spec) with
// spec_source:"image", or null when no image / low confidence / error.
export async function analyzeProductImage(imageUrl, {
  _fetch = globalThis.fetch,
  _vision = callLLMVision,
  minConfidence = 0.4,
} = {}) {
  if (!imageUrl) return null;
  let path;
  try {
    path = await downloadImage(imageUrl, _fetch);
    const r = await _vision({ call_site: "image_spec", prompt: VISION_PROMPT, imagePath: path });
    const confidence = typeof r.confidence === "number" ? r.confidence : 0;
    if (confidence < minConfidence) return null;
    return {
      package_size_l: r.package_size_l ?? null,
      package_size_kg: r.package_size_kg ?? null,
      concentration_pct: r.concentration_pct ?? null,
      active_ingredient: r.active_ingredient ?? null,
      form: r.form ?? null,
      dimensions_cm: r.dimensions_cm ?? null,
      confidence,
      spec_source: "image",
    };
  } catch {
    return null;
  } finally {
    if (path) {
      // Best-effort cleanup of the temp file + its dir.
      await unlink(path).catch(() => {});
    }
  }
}
