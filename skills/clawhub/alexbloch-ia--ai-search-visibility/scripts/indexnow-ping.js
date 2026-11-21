#!/usr/bin/env node
/**
 * IndexNow ping — submits your own sitemap URLs to the IndexNow endpoint.
 *
 * IndexNow is a push protocol: it feeds the index behind several assistants'
 * search layer, which is otherwise pull-only and slow. This is the only push
 * channel available in this skill.
 *
 * NETWORK: this is the ONLY file here that touches the network. It POSTs
 * public URLs read from your own sitemap.xml to api.indexnow.org. It sends
 * no page content, no analytics, no personal data. Run it deliberately.
 *
 * KEY HANDLING: the key is read from the environment, never hardcoded.
 * It is "public by design" (you serve it at the domain root), but hardcoding
 * it into the script + the docs + a build passthrough is what turns a
 * rotatable key into three commits you have to hunt down later. Env only.
 *
 *   export INDEXNOW_KEY=$(node -e "console.log(require('crypto').randomBytes(16).toString('hex'))")
 *   printf '%s' "$INDEXNOW_KEY" > "site/${INDEXNOW_KEY}.txt"   # serve at root
 *
 * Do NOT commit that file: its NAME is the key, so committing it commits the
 * key and freezes it in history across rotations. Gitignore it and emit it
 * from the build step that reads $INDEXNOW_KEY.
 *
 * Usage:
 *   node scripts/indexnow-ping.js                 # every URL in sitemap.xml
 *   node scripts/indexnow-ping.js https://a/ https://b/   # specific URLs
 *
 * ENV: INDEXNOW_KEY, INDEXNOW_HOST (both required — skips cleanly if unset).
 *      SITEMAP_PATH (optional, default ./site/sitemap.xml relative to the
 *      working directory you run this from, NOT to this file's location).
 *
 * EXIT CODES: always 0. Every failure path resolves without throwing, so a
 * third party being down can never fail your deploy. Belt and braces: append
 * `|| true` to the build command anyway.
 */

'use strict';

const fs = require('fs');
const path = require('path');
const https = require('https');

const KEY = process.env.INDEXNOW_KEY;
const HOST = process.env.INDEXNOW_HOST;
// Relative to the project you run this from — never to this file's install dir.
const SITEMAP_PATH = process.env.SITEMAP_PATH
  ? path.resolve(process.cwd(), process.env.SITEMAP_PATH)
  : path.resolve(process.cwd(), 'site/sitemap.xml');

const CHUNK = 1000;      // protocol allows more; stay well inside it
const TIMEOUT_MS = 10000;

function urlsFromSitemap() {
  if (!fs.existsSync(SITEMAP_PATH)) {
    console.warn(
      `[indexnow] No sitemap at ${SITEMAP_PATH} (non-fatal). ` +
        'Set SITEMAP_PATH=/path/to/sitemap.xml, or pass URLs as arguments: ' +
        'node scripts/indexnow-ping.js https://example.com/ https://example.com/page/'
    );
    return [];
  }
  const xml = fs.readFileSync(SITEMAP_PATH, 'utf8');
  return [...xml.matchAll(/<loc>([^<]+)<\/loc>/g)].map((m) => decodeEntities(m[1].trim()));
}

// <loc> content is XML-escaped: the sitemap protocol REQUIRES `&` to be written
// `&amp;`. Submitting the raw match sends `?a=1&amp;b=2` — a URL that has never
// existed on your site. The endpoint answers 200 and indexes nothing: the failure
// is silent, which is why this is decoded here rather than trusted to the regex.
// `&amp;` is unescaped last, so `&amp;lt;` decodes to `&lt;` and not to `<`.
function decodeEntities(s) {
  return s
    .replace(/&lt;/g, '<')
    .replace(/&gt;/g, '>')
    .replace(/&quot;/g, '"')
    .replace(/&apos;/g, "'")
    .replace(/&#39;/g, "'")
    .replace(/&amp;/g, '&');
}

function submit(urls) {
  const payload = JSON.stringify({
    host: HOST,
    key: KEY,
    keyLocation: `https://${HOST}/${KEY}.txt`,
    urlList: urls,
  });

  const opts = {
    method: 'POST',
    hostname: 'api.indexnow.org',
    path: '/indexnow',
    headers: {
      'Content-Type': 'application/json; charset=utf-8',
      'Content-Length': Buffer.byteLength(payload),
    },
  };

  // Resolves on every path. Never rejects, never throws.
  return new Promise((resolve) => {
    const req = https.request(opts, (res) => {
      let body = '';
      res.on('data', (c) => (body += c));
      res.on('end', () => {
        console.log(`[indexnow] HTTP ${res.statusCode} (${urls.length} URLs)`);
        if (res.statusCode === 403) {
          console.warn(
            '[indexnow] 403 = domain not yet validated on the engine console. ' +
              'The script is fine. Declare the key there, then re-run. ' +
              'Your sitemap covers crawl meanwhile.'
          );
        } else if (res.statusCode >= 400) {
          console.warn(`[indexnow] Body: ${body.slice(0, 200)}`);
        }
        resolve();
      });
    });
    req.on('error', (err) => {
      console.warn(`[indexnow] Network error (non-fatal): ${err.message}`);
      resolve();
    });
    req.setTimeout(TIMEOUT_MS, () => {
      console.warn(`[indexnow] Timeout after ${TIMEOUT_MS}ms (non-fatal).`);
      req.destroy();
      resolve();
    });
    req.write(payload);
    req.end();
  });
}

async function main() {
  if (!KEY || !HOST) {
    console.warn(
      '[indexnow] INDEXNOW_KEY and INDEXNOW_HOST must be set in the env. ' +
        'Skipping (non-fatal).'
    );
    return;
  }
  const cliUrls = process.argv.slice(2);
  const urls = cliUrls.length > 0 ? cliUrls : urlsFromSitemap();
  if (urls.length === 0) {
    console.log('[indexnow] No URLs to submit. Exiting.');
    return;
  }
  console.log(`[indexnow] Submitting ${urls.length} URLs to api.indexnow.org…`);
  for (let i = 0; i < urls.length; i += CHUNK) {
    await submit(urls.slice(i, i + CHUNK));
  }
}

main().catch((err) => {
  console.warn(`[indexnow] Fatal error caught (non-fatal): ${err.message}`);
});
