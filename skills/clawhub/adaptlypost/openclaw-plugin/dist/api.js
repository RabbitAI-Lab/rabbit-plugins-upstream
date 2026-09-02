import { readFile, stat } from "node:fs/promises";
import { basename, extname, resolve } from "node:path";
const DEFAULT_BASE_URL = "https://post.adaptlypost.com/post/api/v1";
const TOKEN_PREFIX = "adaptly_";
export function readConfig(api) {
    const root = api.config;
    return root?.plugins?.entries?.["adaptlypost"]?.config ?? {};
}
function requireToken(cfg) {
    if (!cfg.apiToken) {
        throw new Error("No AdaptlyPost API token configured. Set plugins.entries.adaptlypost.config.apiToken. Create a token at https://adaptlypost.com under Settings then API Tokens.");
    }
    if (!cfg.apiToken.startsWith(TOKEN_PREFIX)) {
        throw new Error(`AdaptlyPost API tokens start with "${TOKEN_PREFIX}". The configured value does not, so the API will reject it.`);
    }
    return cfg.apiToken;
}
function buildQuery(params) {
    const search = new URLSearchParams();
    for (const [key, value] of Object.entries(params)) {
        if (value === undefined || value === null)
            continue;
        if (Array.isArray(value)) {
            for (const item of value)
                search.append(key, String(item));
        }
        else {
            search.append(key, String(value));
        }
    }
    const qs = search.toString();
    return qs ? `?${qs}` : "";
}
export async function callApi(cfg, method, path, options = {}) {
    const token = requireToken(cfg);
    const url = `${cfg.baseUrl || DEFAULT_BASE_URL}${path}${options.query ? buildQuery(options.query) : ""}`;
    const res = await fetch(url, {
        method,
        headers: {
            Authorization: `Bearer ${token}`,
            "Content-Type": "application/json",
        },
        body: options.body ? JSON.stringify(options.body) : undefined,
        signal: options.signal,
    });
    const text = await res.text();
    let parsed = text;
    try {
        parsed = text ? JSON.parse(text) : null;
    }
    catch {
        /* non-JSON error body */
    }
    if (!res.ok) {
        if (res.status === 429) {
            const retryAfter = res.headers.get("Retry-After");
            throw new Error(`AdaptlyPost rate limit reached (600 requests per minute per token).${retryAfter ? ` Retry after ${retryAfter}s.` : ""} Wait rather than retrying immediately.`);
        }
        const message = typeof parsed === "object" && parsed !== null && "message" in parsed
            ? String(parsed.message)
            : typeof parsed === "string"
                ? parsed
                : JSON.stringify(parsed);
        throw new Error(`AdaptlyPost API ${res.status}: ${message}`);
    }
    return parsed;
}
const MIME_BY_EXT = {
    ".jpg": "image/jpeg",
    ".jpeg": "image/jpeg",
    ".png": "image/png",
    ".webp": "image/webp",
    ".mp4": "video/mp4",
    ".mov": "video/quicktime",
};
export const SUPPORTED_MIME_TYPES = Object.values(MIME_BY_EXT);
function mimeTypeFor(fileName) {
    const mime = MIME_BY_EXT[extname(fileName).toLowerCase()];
    if (!mime) {
        throw new Error(`Unsupported media type for "${fileName}". AdaptlyPost accepts ${SUPPORTED_MIME_TYPES.join(", ")}.`);
    }
    return mime;
}
async function uploadBuffer(cfg, body, fileName, mimeType, signal) {
    const minted = (await callApi(cfg, "POST", "/upload-urls", {
        body: { files: [{ fileName, mimeType }] },
        signal,
    }));
    const target = minted.urls?.[0];
    if (!target)
        throw new Error("AdaptlyPost did not return an upload URL.");
    const put = await fetch(target.uploadUrl, {
        method: "PUT",
        headers: { "Content-Type": mimeType },
        body: new Blob([body], { type: mimeType }),
        signal,
    });
    if (!put.ok) {
        throw new Error(`Upload to storage failed (${put.status}). The media is not stored, so create_post would reject it.`);
    }
    return { publicUrl: target.publicUrl, key: target.key };
}
export async function uploadLocalFile(cfg, filePath, signal) {
    const file = resolve(filePath);
    const info = await stat(file).catch(() => null);
    if (!info?.isFile())
        throw new Error(`File not found: ${file}`);
    const name = basename(file);
    return uploadBuffer(cfg, await readFile(file), name, mimeTypeFor(name), signal);
}
export async function uploadRemoteUrl(cfg, sourceUrl, signal) {
    const res = await fetch(sourceUrl, { signal });
    if (!res.ok) {
        throw new Error(`Failed to download ${sourceUrl}: ${res.status} ${res.statusText}`);
    }
    const name = sourceUrl.split(/[?#]/)[0].split("/").pop() || "upload";
    const body = new Uint8Array(await res.arrayBuffer());
    return uploadBuffer(cfg, body, name, mimeTypeFor(name), signal);
}
