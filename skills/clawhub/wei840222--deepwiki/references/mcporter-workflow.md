# DeepWiki via mcporter

## Discover a route and query a public repo

Use the installed `mcporter`; check `mcporter list --help` and `mcporter call --help` if a flag is unavailable. Start Bash in this skill directory (or source [the helper](../scripts/deepwiki.sh) by its actual absolute path). Only probe configured servers you trust. Discovery reads aliases without printing their configuration. `DEEPWIKI_MCP_SERVER` prioritizes a configured alias; passing known trusted aliases to `dw_discover` limits the candidates to those aliases in order. `DEEPWIKI_MCPORTER_CONFIG` selects a config for both discovery and configured calls. No config changes or OAuth initiation are needed.

```bash
source scripts/deepwiki.sh
repo=$(dw_public_repo kubernetes/kubernetes) || exit 1
route=$(dw_discover) || exit 1
dw_structure "$route" "$repo" || exit 1
dw_ask "$route" "How do the scheduling and binding cycles differ? Cite upstream files." "$repo"
```

The helper verifies GitHub visibility on each tool call, follows HTTPS redirects, and sends only GitHub’s canonical public `full_name`. Stop on non-200, malformed JSON, or absent public confirmation. Do not send known private names even to the preflight. A GitHub `404` does not establish whether a repository is private or absent.

Discovery calls `mcporter list <server> --schema --json --no-oauth --timeout 8000 --exit-code` and returns the exact tool names for a complete direct or `DeepWiki-` family. The live public endpoint and the tested gateway both use `ask_wiki_question`; an older `ask_question` is accepted only if it actually appears in `tools/list`. Keep the selected route for the task. Pass the next trusted candidate explicitly on a transient transport failure; do not blindly retry auth, rate-limit, or repository errors across providers.

## Parameters and results

| Capability | Arguments | Result |
| --- | --- | --- |
| `read_wiki_structure` | `{repoName: "owner/repo"}` | Wiki topic tree. Check that the relevant subsystem appears. |
| `ask_wiki_question` (or live `ask_question`) | `{repoName, question}`; tested schemas allow a string or up to 10 repo names | Generated answer, sometimes relative `/wiki/...` links and a `https://deepwiki.com/search/...` link. Resolve those relative links on `https://deepwiki.com`; confirm source paths before using them as evidence. |
| `read_wiki_contents` | `{repoName: "owner/repo"}` | Full generated wiki. Schema discovery does not download it. |

`--output json` returned `{"result":"..."}` for both tested routes. The helper also accepts a nonempty JSON string, `structuredContent.result`, or MCP text blocks; it rejects JSON errors, `isError: true`, unrecognized shapes, and empty text. A nonempty result can still be an unavailable-wiki message or an inadequate answer; read it before citing.

For a focused cross-repo question, pass each approved public repository as a separate argument. The helper refuses multi-repo input when the schema does not advertise an array and sends nothing to DeepWiki if any repository is unverified. Use multiple repositories only when the answer needs them.

```bash
dw_ask "$route" "How do their extension points differ at a high level? Cite each repository separately." \
  kubernetes/kubernetes gohugoio/hugo
```

For an explicitly approved full-wiki request only, capture the output instead of sending it straight to chat:

```bash
(umask 077; dw_contents "$route" "$repo" --allow-full > deepwiki-full.md)
```

## Troubleshooting

- **No configured match or transient connection failure:** keep the CLI diagnostic; a failed handshake is not an empty wiki. Try the other trusted configured candidate once, then use [the direct public route](api-fallback.md) for a confirmed public repository or read upstream sources.
- **HTTP 401/403 or OAuth required:** stop this MCP route, report the auth error, and use public sources for public repos. Do not initiate OAuth, retry with other credentials, or route private data to public DeepWiki.
- **HTTP 429:** respect a valid `Retry-After` once within the task budget. If missing, wait one second for at most one retry; if throttled again or the requested wait exceeds the budget, use upstream source or report the limit. Do not fan out retries.
- **Tool/schema drift:** re-read the specific live schema once. Use the exact advertised name and shape; do not guess a different spelling based on a generated page.
- **Sparse wiki, unavailable repo, or no source references:** confirm canonical name and topics, ask one narrower question, then read public source or docs. Stop full-wiki extraction if the result is too large; do not retry it unbounded.

## Smoke evidence

The configured gateway returned topic trees for `kubernetes/kubernetes` and `gohugoio/hugo`. Three focused Q&A calls returned nonempty `result` strings: Kubernetes scheduling vs binding cycles, Hugo’s Goldmark provider/default, and Hugo shortcode delimiter behavior. Cross-checks: [Kubernetes scheduling framework](https://kubernetes.io/docs/concepts/scheduling-eviction/scheduling-framework/), [Hugo converter registry](https://github.com/gohugoio/hugo/blob/master/markup/markup.go), [Hugo default markup configuration](https://github.com/gohugoio/hugo/blob/master/markup/markup_config/config.go), and [Hugo shortcode notation](https://gohugo.io/content-management/shortcodes/). The public `/mcp` route also returned Hugo’s structure. Full-wiki download is not part of this smoke test.

For Devin-managed wiki steering, see the [official `.devin/wiki.json` reference](https://docs.devin.ai/work-with-devin/deepwiki). Both `repo_notes` and a nonempty `pages` array are required when that config is present; the specified pages replace the default page plan. Editing it is a separate repository change.
