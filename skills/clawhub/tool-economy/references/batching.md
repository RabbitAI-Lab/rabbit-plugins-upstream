# Batching Independent Tool Calls

The single highest-impact economy technique: **issue independent calls in the
same turn.** Most agent runtimes execute independent tool calls concurrently, so
batching collapses N round-trips into one.

## What "Independent" Means

Call B is *independent* of call A if B does not need A's output to be formed.
You can write out all N calls before seeing any result.

| Independent (batch)             | Dependent (serial)                          |
|---------------------------------|---------------------------------------------|
| Read 3 unrelated files          | Read file → patch line found in it          |
| Fetch 5 URLs                    | Search web → extract top result             |
| Run tests + lint + typecheck    | Read config → run build with that config    |
| `git status` + `git log` + `git diff` | `git add` → `git commit` → `git push` |

## How to Batch

1. Scan your planned next steps.
2. Partition into "rounds": each round contains calls whose inputs are already
   known.
3. Issue each round as a single assistant turn with multiple tool calls.

### Example: Inspecting a Repo Before a Change

**Wasteful (5 serial turns):**
```
T1: read_file(package.json)
T2: read_file(tsconfig.json)
T3: search_files("TODO", target=content)
T4: terminal("git log --oneline -5")
T5: search_files("*.test.ts", target=files)
```

**Economical (1 turn, 5 parallel calls):**
```
T1: [ read_file(package.json),
      read_file(tsconfig.json),
      search_files("TODO"),
      terminal("git log --oneline -5"),
      search_files("*.test.ts", target=files) ]
```

Same information, ~5× lower wall-clock latency, same token cost for the calls
themselves (but far fewer reasoning tokens between turns).

## Pitfalls

- **False independence:** if call B's *arguments* depend on call A's result, you
  cannot batch them. Re-check each pair.
- **Resource contention:** two heavy `terminal` builds may fight for CPU. Stagger
  if needed, but most read-only calls (file reads, searches, web fetches) are
  safe to parallelize freely.
- **Token budget per turn:** batching more calls grows the single response. If a
  batch would be enormous, split into a few medium rounds rather than one huge
  turn.

## Rule of Thumb

> If you can write all the calls before any of them returns, they belong in the
> same turn.
