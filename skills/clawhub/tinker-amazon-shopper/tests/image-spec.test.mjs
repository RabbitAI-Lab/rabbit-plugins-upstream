import test from "node:test";
import assert from "node:assert/strict";
import { analyzeProductImage } from "../scripts/image-spec.mjs";

function fakeFetchOk() {
  return async () => ({
    ok: true,
    status: 200,
    arrayBuffer: async () => new Uint8Array([0xff, 0xd8, 0xff]).buffer, // tiny fake jpeg
  });
}

test("returns null when no image url", async () => {
  const r = await analyzeProductImage(null, { _fetch: fakeFetchOk(), _vision: async () => ({}) });
  assert.equal(r, null);
});

test("reads spec from image when vision confident", async () => {
  const vision = async ({ call_site, imagePath }) => {
    assert.equal(call_site, "image_spec");
    assert.match(imagePath, /product\.jpg$/);
    return {
      package_size_l: 20, package_size_kg: 25, concentration_pct: 15,
      active_ingredient: "sulfuric acid", form: "liquid",
      dimensions_cm: "40x30x20", confidence: 0.85,
    };
  };
  const r = await analyzeProductImage("https://m.media-amazon.com/images/I/x.jpg", { _fetch: fakeFetchOk(), _vision: vision });
  assert.equal(r.spec_source, "image");
  assert.equal(r.package_size_l, 20);
  assert.equal(r.concentration_pct, 15);
  assert.equal(r.active_ingredient, "sulfuric acid");
  assert.equal(r.dimensions_cm, "40x30x20");
});

test("returns null when vision confidence below threshold", async () => {
  const vision = async () => ({ package_size_l: null, confidence: 0.2 });
  const r = await analyzeProductImage("https://m.media-amazon.com/images/I/x.jpg", { _fetch: fakeFetchOk(), _vision: vision });
  assert.equal(r, null);
});

test("returns null on download error (graceful)", async () => {
  const badFetch = async () => ({ ok: false, status: 404 });
  const r = await analyzeProductImage("https://m.media-amazon.com/images/I/x.jpg", { _fetch: badFetch, _vision: async () => ({ confidence: 1 }) });
  assert.equal(r, null);
});

test("returns null on vision error (graceful)", async () => {
  const vision = async () => { throw new Error("vision boom"); };
  const r = await analyzeProductImage("https://m.media-amazon.com/images/I/x.jpg", { _fetch: fakeFetchOk(), _vision: vision });
  assert.equal(r, null);
});
