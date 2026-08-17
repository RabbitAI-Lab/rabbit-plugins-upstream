# Search Strategies (the Locate Phase)

The Locate phase runs **multiple query passes**, because artifacts are rarely filed under the first word you reach for. This doc is the full playbook.

## Pass order

Run passes in this order. Each later pass only runs if the earlier ones didn't surface a high-confidence hit.

1. **Exact / keyword** — highest precision, lowest recall. The literal error string, function name, filename, or config key.
2. **Semantic-adjacent** — paraphrase the intent. If the exact term misses, the concept may be filed under different words.
3. **Structural** — look for *code blocks*, *diffs*, or *command outputs* near the topic, not just prose. Solutions hide inside fenced blocks.
4. **Temporal** — constrain to the window when the work happened, then re-run keyword. Narrows a noisy corpus to the relevant stratum.

## 1. Exact / keyword

Use the **literal token** the artifact would contain:

- An exception → the exact exception class and message fragment.
- A function → its name.
- A config value → the key name.
- A CLI failure → the exact stderr fragment.

```
# exact, high-precision
query: "connectionpool value too many connections"
query: "AttributeError: 'NoneType' object has no attribute 'split'"
```

**Pitfall:** exact pass misses when the user paraphrased the error in their message but the stack trace was elided. Always follow with semantic-adjacent.

## 2. Semantic-adjacent

Paraphrase the **intent**, not the token. Think: "if I didn't remember the exact word, how would I describe this?"

| Concept | Exact miss | Semantic seed |
|---|---|---|
| OOM kill | `"OOMKilled"` | `"memory limit pod restarted"` |
| Race condition | `"concurrent modification"` | `"intermittent wrong order flaky"` |
| Cert expiry | `"x509: certificate has expired"` | `"tls handshake failed clock skew"` |
| Port conflict | `"Address already in use"` | `"cannot bind port already listening"` |

`excavate.py` does keyword matching; for the semantic pass use `session_search` (FTS5) or any embedding search over the corpus.

## 3. Structural (code-block) pass

The fix is often inside a fenced code block whose prose doesn't repeat the keyword. `excavate.py --extract code` pulls every fenced block from matching sessions and re-ranks by proximity to the query terms.

When to prioritize this pass:

- You remember the *shape* of the answer (a shell one-liner, a YAML snippet) but not the words around it.
- The keyword appears only in code comments or command output, never in prose.
- The session is a wall of debugging chat with the fix buried in one block.

## 4. Temporal pass

Constrain to a date window, then re-run keyword. Two modes:

- **`--after` / `--before`** on `excavate.py` filters by file mtime or, if the session has frontmatter, the session date.
- **Relative** ("sessions from the week we shipped v2") — convert to absolute dates first.

Temporal narrowing is how you separate the *original* fix from the *five times someone re-asked about it later*. The earliest high-scoring session in the window is usually the source.

## Query expansion

When keyword + semantic both miss, expand the query:

- **Synonyms:** `rebalance` → `rebalancing`, `rebalance`, `coordinator`, `consumer group`.
- **Hyponyms:** `kafka` → `producer`, `consumer`, `broker`, `topic`, `partition`.
- **Surrounding nouns:** the files, services, or libraries adjacent to the problem.

Expansion trades precision for recall. Run it last, and require a resolution marker (Phase 3 signal) to trust any expanded hit.

## Negation

To find a session that discusses X but **not** Y (e.g., "redis caching" but not "sidekiq"):

```bash
python3 scripts/excavate.py dig ./sessions --query "redis cache" --not "sidekiq"
```

Negation is useful for disambiguating overloaded terms (e.g., "migration" the DB step vs. "migration" the framework).

## Picking the number of passes

| Confidence after pass N | Action |
|---|---|
| Pass 1 returns a session with a resolution marker | Stop. Extract. |
| Pass 1 returns dense hits but no resolution marker | Run pass 2 to confirm. |
| Pass 1 misses or is sparse | Run pass 2, then 3. |
| Passes 1–3 all miss | Run pass 4 (temporal), then query expansion. |
| All passes miss | The artifact may not exist. Say so — don't fabricate. |

## Anti-patterns

- **Single-query dig.** One search, one answer. This is grep, not archaeology. Always run ≥ 2 passes unless pass 1 returns a resolution.
- **Keyword worship.** Refusing to paraphrase because "the error message is the error message." The error message may not be in the transcript.
- **Ignoring structure.** Reading only prose and missing the fenced block that contains the actual fix.
- **No temporal filter on noisy corpora.** A term that appears in 200 sessions needs narrowing; use the date window.
- **Treating expansion hits as gospel.** Expanded queries have low precision. Require a resolution marker before trusting.
