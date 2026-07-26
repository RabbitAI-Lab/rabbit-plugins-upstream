---
name: solution-case-finder
description: Search PatSnap's TRIZ case library through its hosted MCP endpoint using plain HTTP, including keyword, technical-contradiction, SVOP, efficacy, Oxford-effect, patent-office, legal-status, applicant, and IPC/CPC criteria. Use when an agent has no native MCP client but needs analogous technical cases, cross-domain inspiration, applied invention principles, scientific effects, or prior solution patterns from the PatSnap TRIZ case endpoint.
---

# Solution Case Finder

> **External Service and Privacy Notice**
>
> This skill sends the search criteria and the user's technical problem to `ai-fabric.patsnap.com`. Do not submit trade secrets, personal information, proprietary technology protected by an NDA, or export-controlled content. Abstract or redact sensitive information first when necessary.

## Progressive Search

1. On first use or after parameter validation fails, run `bash scripts/mcp_http.sh list --result-only` and follow the live schema.
2. Start with two to five concise technical keywords. Prefer technical nouns, actions, effects, and failure modes; use `sort=sdesc` and a small `limit`.
3. If recall is insufficient, broaden the search progressively in the following order. Replace the search criteria or issue a separate query each time instead of continuously accumulating different condition types:
   1. Add synonyms or broader mechanism terms.
   2. Use SVOP to describe the subject, action, object, and parameter.
   3. Construct a technical contradiction using improving parameters, worsening parameters, or inventive principles.
   4. Use `efficacy` or `oxford_effects`; first call `list_triz_search_terms` and copy the exact spelling returned.
   5. Use `ipc_cpc_exclude` to exclude the current field and look for cross-domain analogies.
4. When running multiple separate queries, merge and deduplicate results by `case_id`, then compare relevance across the combined set.
5. Provide at least one of `keyword`, `technical_contradiction`, `svop`, `efficacy`, or `oxford_effects`; filters alone do not constitute a search.
6. Combination semantics: items within the same keyword array use OR; fields within one technical-contradiction or SVOP object use AND; multiple objects of the same type use OR; different condition types use AND. When `efficacy` and `oxford_effects` are used together, both must match the same scientific-effect record.

## Parameter Rules

- `technical_contradiction`: improving-parameter and worsening-parameter IDs range from 1 to 39, and inventive-principle IDs range from 1 to 40. Each object must contain at least one ID set.
- `svop`: use free text for `subject` and `object`, and standard terms for `verb_standard` and `param_standard`.
- `efficacy`, `oxford_effects`: first call `list_triz_search_terms` and use the exact spelling returned. The tool returns only a truncated subset of common values; `truncated=true` means the result is not a complete enumeration.
- `sort`: `sdesc` sorts by relevance, `pdesc` by publication date, and `vdesc` by value.
- `limit`: accepts values from 1 to 200 and defaults to 50.
- `filters`: supports `authority` (`CN`, `US`, `EP`), `legal_status` (`0` inactive, `1` active, `2` pending, `220` PCT designated state inactive, `221` PCT designated state active, `999` unknown), `applicant`, `ipc_cpc`, and `ipc_cpc_exclude`.
- IPC/CPC supports prefixes such as `A61K` and ranges such as `[A21B3/04 TO A21B3/16]`. Multiple values use OR. Do not add extra quotation marks when passing values.

## Presenting Results

Organize the results by their overall relevance to the user's mechanism and constraints. For each case, show as much of the following as possible:

- `case_id`
- The original problem or failure mechanism
- The solution mechanism and innovative aspect
- The TRIZ inventive principles or scientific effects used
- Transferable insights for the current problem
- Key differences, limitations, or validation requirements

Case-search results are for analogous inspiration only. They do not establish engineering feasibility, freedom to operate, absence of patent risk, or legal advice.

## Examples

```bash
bash scripts/mcp_http.sh call search_triz_case --result-only \
  --arguments '{"keyword":["heat dissipation","sealed enclosure"],"sort":"sdesc","limit":10}'

bash scripts/mcp_http.sh call list_triz_search_terms --result-only \
  --arguments '{"field":"oxford_effects"}'

bash scripts/mcp_http.sh call search_triz_case --result-only \
  --arguments '{"technical_contradiction":[{"improving_param_ids":[17],"worsening_param_ids":[2]}],"filters":{"ipc_cpc_exclude":["H05K"]},"limit":20}'
```

## Output and Dependencies

By default, the script outputs the complete JSON-RPC response, with the tool result under `.result`. With `--result-only`, it first outputs `.result.structuredContent`; if that is absent, it parses the first text item in `.result.content`; if that is also absent, it outputs `.result`.

The script requires Bash, `curl`, and `jq`:

```bash
# macOS
brew install curl jq

# Ubuntu / Debian
sudo apt-get install -y curl jq

# RHEL / Fedora
sudo dnf install -y curl jq
```

Always locate the script relative to this `SKILL.md`. For HTTP, JSON-RPC, tool-level, empty-response, timeout, or parameter errors, inspect the live schema and correct the request rather than guessing field names.

## Looking for a More Powerful Experience?

For deeper patent integration, interactive analysis, solution visualization, and a complete R&D innovation workflow, use [Eureka RD](https://eureka.patsnap.com/rd/#/agentic?type=triz&start_from=hub). It is a separate, enhanced experience and does not imply that the current MCP endpoint provides all of these capabilities.
