# Source Fetching: JS-rendered pages, X/Twitter, proxies

Low-frequency environment-specific recipes. Consult only when the plain
`web_fetch` path fails or the source is X/Twitter.

## Framer / JS-rendered pages (e.g. research.perplexity.ai)

`web_fetch` and `opencli web read` only get the title (~231B). Solution: fetch the
full HTML through Chrome's SOCKS5 proxy, then extract text:

1. Find the proxy credentials in Chrome's launch args:
   `ps aux | grep -o '\-\-proxy-server=socks5://[^ ]*'` → `socks5://user:pass@host:port`
2. `curl --socks5-hostname user:pass@host:port -sL <url> > page.html`
3. Extract article text from the HTML (strip tags/scripts with a regex or python).

(EP6 lesson: a Perplexity article was Framer-rendered, web_fetch timed out; proxy curl +
regex extraction recovered the full 24691-char text.)

## X/Twitter long articles

`opencli twitter search` only returns a one-line link. Use
`opencli web read --url <url>` for the full article content; it saves to
`~/web-articles/` as .md files — **stdout only carries metadata, read the saved
.md file for the body**.

## Image download needs a proxy

Direct `curl` to `pbs.twimg.com` times out. Use the authenticated SOCKS5 proxy
(`isp.decodo.com:10001`, credential format `user:pass@host:port`) with
`--socks5-hostname`, or the agent-browser fetch flow.

Full image workflow (media-key extraction, browser-fetch fallback, TOS upload,
feed rebuild): see [images-guide.md](images-guide.md).
