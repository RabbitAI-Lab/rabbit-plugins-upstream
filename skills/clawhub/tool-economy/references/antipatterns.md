# Anti-Patterns Catalog

Common ways agents waste tool budget, and the economy pattern that replaces each.

---

## AP-1: Serial Cascade of Independent Reads

**Symptom:** Three `read_file` calls in three separate turns.

**Cost:** 2 extra round-trips of latency + 2 extra reasoning passes.

**Fix:** Batch into one turn. See `batching.md`.

---

## AP-2: Re-Reading a Static File

**Symptom:** `read_file(config.yaml)` in turn 3, again in turn 7, with no edit
in between.

**Cost:** 1 redundant call (tokens + latency) for stale-identical data.

**Fix:** Reuse the content already in context. Re-read only after the file is
known to have changed (e.g. you patched it, or an external mtime check differs).

---

## AP-3: Weak Command Chains

**Symptom:**
```
terminal("grep -rn foo .")
terminal("grep -rn foo . | wc -l")
terminal("find . -name '*.py'")
```

**Cost:** 3 calls for what one `search_files` call returns.

**Fix:** Use the powerful built-in:
```
search_files("foo", target=content, output_mode=count)
```

---

## AP-4: Read-Then-Patch-Then-Read

**Symptom:** Read a file, patch one line, then read the whole file again to
"verify."

**Cost:** 1 redundant full-file read. The patch result already tells you the new
content.

**Fix:** Trust the patch output (or diff). Re-read only a *specific* region if
you must confirm layout, not the whole file.

---

## AP-5: Exploratory Ping-Pong

**Symptom:** Alternating `search_files` → `read_file` → `search_files` →
`read_file` across many turns without a plan.

**Cost:** Many small calls, high latency, low signal.

**Fix:** Do a single broad search (or a batched set of searches) up front, then
batch-read the relevant files, then act. Plan the exploration before executing.

---

## AP-6: Re-Fetching External Data

**Symptom:** `web_extract(url)` called twice for the same URL in one session.

**Cost:** Network latency + tokens for identical content.

**Fix:** Cache the result in context. Re-fetch only if the source is
time-sensitive (news, prices, live status) and enough time has passed.

---

## AP-7: Confirm-Then-Do

**Symptom:**
```
T1: terminal("ls")           # "is the file there?"
T2: terminal("cat file")     # "ok read it"
```

**Cost:** 1 extra call to confirm something the actual operation would have
reported anyway.

**Fix:** Just attempt the real operation; handle the error if it fails. Most
tools return clear errors for missing files/paths.

---

## AP-8: Forgetting `replace_all`

**Symptom:** Five separate `patch` calls to rename one identifier in five spots.

**Cost:** 4 extra calls.

**Fix:** One `patch(..., replace_all=true)` or a single targeted sed via
`terminal`.

---

## AP-9: Human-Style Click-Through

**Symptom:** Navigating a browser one click at a time when a direct URL or API
call would do.

**Cost:** Many slow browser round-trips.

**Fix:** Prefer `web_extract` / direct API / direct URL navigation over
incremental UI clicks.

---

## AP-10: No Budget, No Awareness

**Symptom:** Agent never estimates or counts calls; "just keeps going."

**Cost:** Unbounded waste; no trigger to replan.

**Fix:** Set a budget (see `budgeting.md`), tally as you go, stop when over.
