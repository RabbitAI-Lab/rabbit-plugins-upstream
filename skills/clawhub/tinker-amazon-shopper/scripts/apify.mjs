// apify.mjs — Apify Amazon Product Scraper actor adapter.
//
// Apify is a marketplace of containerized scrapers ("actors"). Their Amazon
// Product Scraper actor handles WAF, captchas, proxies, and returns
// structured JSON. The free tier ($0/mo + $5 credit, no card) covers
// ~5,000 Amazon product lookups per month — well within this skill's
// shopping use case.
//
// Env vars (token is required; the rest have defaults):
//   AMAZON_SHOPPER_APIFY_TOKEN          — Personal API token (Apify Settings → Integrations)
//   AMAZON_SHOPPER_APIFY_SEARCH_ACTOR   — Actor id for keyword search (default: junglee/amazon-crawler)
//   AMAZON_SHOPPER_APIFY_DETAIL_ACTOR   — Actor id for product detail (default: junglee/amazon-crawler — same actor, different input)
//   AMAZON_SHOPPER_APIFY_DOMAIN         — Amazon marketplace (default: amazon.es)
//   AMAZON_SHOPPER_APIFY_ASSOCIATE_TAG  — Optional; appended to product URLs so clicks credit your Associates tag
//
// Activation: when AMAZON_SHOPPER_APIFY_TOKEN is set, shopper.mjs prefers
// this module. Apify > Creators API > HTML fetcher (the last is currently
// WAF-blocked from this gateway IP; honest exit).

const DEFAULT_SEARCH_ACTOR = "junglee/amazon-crawler";
const DEFAULT_DETAIL_ACTOR = "junglee/amazon-crawler";
const DEFAULT_DOMAIN = "amazon.es";
const API_BASE = "https://api.apify.com/v2";

export function apifyConfigured() {
  return Boolean(process.env.AMAZON_SHOPPER_APIFY_TOKEN);
}

function getConfig() {
  const token = process.env.AMAZON_SHOPPER_APIFY_TOKEN;
  if (!token) throw new Error("Apify not configured (AMAZON_SHOPPER_APIFY_TOKEN missing).");
  return {
    token,
    searchActor: process.env.AMAZON_SHOPPER_APIFY_SEARCH_ACTOR || DEFAULT_SEARCH_ACTOR,
    detailActor: process.env.AMAZON_SHOPPER_APIFY_DETAIL_ACTOR || DEFAULT_DETAIL_ACTOR,
    domain: process.env.AMAZON_SHOPPER_APIFY_DOMAIN || DEFAULT_DOMAIN,
    associateTag: process.env.AMAZON_SHOPPER_APIFY_ASSOCIATE_TAG || null,
  };
}

function actorPath(actorId) {
  return actorId.replace("/", "~");
}

async function runActorSync(actorId, input, { token, _fetch = globalThis.fetch }) {
  const url = `${API_BASE}/acts/${actorPath(actorId)}/run-sync-get-dataset-items?token=${encodeURIComponent(token)}`;
  const res = await _fetch(url, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(input),
  });
  if (!res.ok) {
    const body = await res.text();
    throw new Error(`Apify actor ${actorId} failed: HTTP ${res.status} — ${body.slice(0, 300)}`);
  }
  return await res.json();
}

function appendAssociateTag(url, tag) {
  if (!tag || !url) return url;
  try {
    const u = new URL(url);
    if (!u.searchParams.has("tag")) u.searchParams.set("tag", tag);
    return u.toString();
  } catch {
    return url;
  }
}

// SearchItems — keyword → product[]. Same shape as extract-search.mjs:extractSearchResults().
export async function searchItems(keywords, { maxProducts = 10, _fetch = globalThis.fetch } = {}) {
  const cfg = getConfig();
  const items = await runActorSync(
    cfg.searchActor,
    {
      categoryOrProductUrls: [
        { url: `https://www.${cfg.domain}/s?k=${encodeURIComponent(keywords)}` },
      ],
      maxItemsPerStartUrl: Math.min(50, maxProducts),
      proxyCountry: "ES",
      // Pull product detail (price, description, specs) for search results so
      // rank has enough to work with — false here means listing-only no prices.
      scrapeProductDetails: true,
    },
    { token: cfg.token, _fetch },
  );
  return mapSearchResponseToProducts(items, cfg.associateTag);
}

function mapSearchResponseToProducts(items, associateTag) {
  if (!Array.isArray(items)) return [];
  return items
    .filter((item) => item && (item.asin || item.ASIN))
    .map((item, i) => {
      const asin = String(item.asin || item.ASIN);
      const rawUrl = item.url || item.productUrl || `https://www.amazon.es/dp/${asin}/`;
      const sellerName = item.seller?.name ?? null;
      // "Sold by Amazon" = lowest refund friction (instant A-to-z, free return).
      // Third-party is still A-to-z-covered for "not as described" but may need
      // a 48h seller-contact wait + escalation. See SKILL.md "Refund strategy".
      const sellerIsAmazon = sellerName
        ? /^amazon(\.|\s|$|eu|\.es|\.com)/i.test(sellerName.trim())
        : null;
      return {
        asin,
        position: i + 1,
        title: item.title || item.name || "",
        url: appendAssociateTag(rawUrl, associateTag),
        image_url: item.thumbnailImage || item.image || item.imageUrl || null,
        current_price_eur: parsePrice(item.price ?? item.priceText ?? item.priceValue),
        list_price_eur: parsePrice(item.listPrice ?? item.originalPrice),
        rating: typeof item.stars === "number" ? item.stars : parseFloat(item.rating) || null,
        review_count: typeof item.reviewsCount === "number" ? item.reviewsCount : parseInt(item.reviewCount, 10) || null,
        is_prime: Boolean(item.isPrime || item.prime),
        is_best_seller: Boolean(item.bestSeller || item.isBestSeller),
        seller_name: sellerName,
        seller_is_amazon: sellerIsAmazon === null ? null : (sellerIsAmazon ? 1 : 0),
        in_stock: item.inStock === false ? 0 : 1,
      };
    });
}

function parsePrice(raw) {
  if (raw == null) return null;
  if (typeof raw === "number") return Number.isFinite(raw) ? raw : null;
  // Nested object shapes (junglee returns these): {value, currency} or {amount, currency}
  if (typeof raw === "object") {
    const candidate =
      raw.value ?? raw.amount ?? raw.current ?? raw.minPrice?.value ?? raw.minPrice?.amount;
    if (typeof candidate === "number") return Number.isFinite(candidate) ? candidate : null;
    if (typeof candidate === "string") raw = candidate;
    else return null;
  }
  let s = String(raw).replace(/[^0-9.,]/g, "");
  if (!s) return null;
  const lastComma = s.lastIndexOf(",");
  const lastDot = s.lastIndexOf(".");
  if (lastComma > lastDot) {
    // Spanish format: "1.234,56" — dot thousands, comma decimal.
    s = s.replace(/\./g, "").replace(",", ".");
  } else if (lastDot > lastComma) {
    // English format: "1,234.56" — comma thousands, dot decimal.
    s = s.replace(/,/g, "");
  }
  const n = parseFloat(s);
  return Number.isFinite(n) ? n : null;
}

// GetItem — detail equivalent. Same shape as extract-detail.mjs:extractDetailSpec().
export async function getItem(asin, { _fetch = globalThis.fetch } = {}) {
  const cfg = getConfig();
  const items = await runActorSync(
    cfg.detailActor,
    {
      productUrls: [{ url: `https://www.${cfg.domain}/dp/${asin}/` }],
      proxyCountry: "ES",
    },
    { token: cfg.token, _fetch },
  );
  const item = Array.isArray(items) ? items[0] : null;
  if (!item) {
    return { title: null, brand: null, weight_kg: null, bullets: [], detail_rows: {}, combined_text: "" };
  }
  const title = item.title || item.productTitle || null;
  const bullets = Array.isArray(item.features) ? item.features : Array.isArray(item.bullets) ? item.bullets : [];
  const brand = item.brand || item.manufacturer || null;
  const detail_rows = {};
  const attributes = item.attributes || item.productInformation || {};
  if (attributes && typeof attributes === "object") {
    for (const [k, v] of Object.entries(attributes)) {
      if (typeof v === "string" && k.length < 60) detail_rows[k.toLowerCase()] = v;
    }
  }
  const weight_kg = inferWeightKg(detail_rows, bullets);
  return {
    title,
    brand,
    weight_kg,
    bullets,
    detail_rows,
    combined_text: [
      title ? `Title: ${title}` : "",
      brand ? `Brand: ${brand}` : "",
      bullets.length ? `Bullets:\n- ${bullets.join("\n- ")}` : "",
      Object.keys(detail_rows).length ? `Details:\n${Object.entries(detail_rows).map(([k, v]) => `- ${k}: ${v}`).join("\n")}` : "",
    ].filter(Boolean).join("\n\n"),
  };
}

function inferWeightKg(rows, bullets) {
  const cands = [];
  for (const [k, v] of Object.entries(rows)) {
    if (/peso|weight|kilogr|\bkg\b/i.test(k)) cands.push(v);
  }
  for (const b of bullets) {
    const m = String(b).match(/([0-9]+(?:[,.]?[0-9]+)?)\s*kg\b/i);
    if (m) cands.push(`${m[1]} kg`);
  }
  for (const c of cands) {
    const n = parsePrice(c);
    if (n && n > 0 && n < 1000) return n;
  }
  return null;
}
