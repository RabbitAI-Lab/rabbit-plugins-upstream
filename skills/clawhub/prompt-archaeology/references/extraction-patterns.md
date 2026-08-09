# Extraction Patterns

The transcript is the **site**, not the **artifact**. Once you've located and scored the winning session, extract the minimal artifact — never dump the whole transcript. This doc gives templates for each artifact type.

## Universal extraction rules

1. **Quote, don't paraphrase.** Use `> ...` blockquotes. The artifact must be the session's words, not your reconstruction.
2. **Three quotes max** (failing state, change, success marker) unless the artifact is inherently longer (a config file).
3. **Cite the session** — path or session id — on every extraction.
4. **Drop the journey.** The eight wrong turns before the fix are not the artifact. They may be relevant for a *rejection* extraction (below), but not for a *fix*.

## 1. Fix extraction

The most common artifact. Three quotes: failing state → change → success marker.

**Template:**

```markdown
> **Failing:** `ConnectionPool exceeded max_connections (50)`
>
> **Change:** set `SQLALCHEMY_POOL_SIZE=20` and `SQLALCHEMY_MAX_OVERFLOW=5` in `.env`
>
> **Resolved:** "spun up the app, hit it with 200 concurrent requests, pool stable — that fixed it"

— `sessions/2024-03-12-db-pool.md`
```

**What to drop:** the forty messages of hypothesis-testing before the config change. They're noise once the fix is known.

## 2. Decision extraction

Two flavors: a decision *with* rationale is valuable; a decision *without* rationale is nearly useless. Always extract both.

**Template:**

```markdown
> **Options considered:** Postgres vs. MongoDB for the ledger
>
> **Chose:** Postgres
>
> **Rationale:** "we need strong consistency for the ledger — eventual consistency
> would mean we could double-spend on a network partition, and that's a
> correctness bug, not a performance bug"

— `sessions/2024-01-08-db-choice.md`
```

**If the rationale isn't in the session,** say so explicitly:

```markdown
> **Chose:** Postgres (rationale not recorded in this session; see sessions/2024-01-09*.md for follow-up)
```

Don't invent a rationale to fill the gap.

## 3. Command / incantation extraction

The exact command plus one line of context. Nothing else.

**Template:**

```markdown
> Concatenate two MP4s without re-encoding:
>
> ```bash
> ffmpeg -i "concat:in1.mp4|in2.mp4" -c copy out.mp4
> ```

— `sessions/2024-05-30-video.md`
```

If the command has prerequisites (a `dep install`, an env var), include them in the same block. If the session showed a *wrong* invocation first, include it only as a `# NOT this:` comment.

## 4. Rejected-approach extraction

Often more valuable than the fix — it saves you from re-walking a dead end.

**Template:**

```markdown
> **Tried:** rewriting the parser as a single regex
>
> **Failed:** "catastrophic backtracking on inputs > 4KB, CPU pinned at 100%"
>
> **Lesson:** nested quantifiers on unbounded input; stick with the recursive-descent parser

— `sessions/2024-02-14-parser.md`
```

**When to extract a rejection:** the session explicitly records *what was tried*, *how it failed*, and (ideally) *why*. If only the failure is recorded with no diagnosis, extract the failure and mark the lesson as inferred.

## 5. Config / architecture extraction

For durable artifacts (config files, architecture diagrams described in prose). Quote the whole relevant block, not a snippet.

**Template:**

```markdown
> nginx config that fixed the 502 on long-polling:
>
> ```nginx
> location /events {
>     proxy_pass http://backend;
>     proxy_read_timeout 3600s;
>     proxy_buffering off;
> }
> ```

— `sessions/2024-04-01-nginx.md`
```

## Anti-patterns

- **The whole transcript.** The user asked for the fix, not the dig diary.
- **Paraphrased fix.** "We changed the pool size" is useless; `SQLALCHEMY_POOL_SIZE=20` is the artifact.
- **Decision without rationale.** "We chose Postgres" answers nothing. Always pair with the *why*.
- **Fix without success marker.** If the session never confirmed the fix worked, say so: "applied but not confirmed in this session."
- **Extracting the first mention.** The first mention of a term is often the *problem statement*, not the fix. Score and read before extracting.
- **Inventing rationale.** If the session doesn't say why, don't fill it in. Mark it missing.
