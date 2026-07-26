# Flush Prompt — openclaw.json Configuration

The memory flush is a silent agentic turn triggered by the platform when the session approaches the context window limit. Configure the flush prompt to provide structure for what gets encoded.

Add to your `openclaw.json`:

```json5
{
  agents: {
    defaults: {
      compaction: {
        memoryFlush: {
          enabled: true,
          softThresholdTokens: 4000,
          prompt: "Pre-compaction memory flush. If this conversation was trivial (single-question lookup, no decisions), reply NO_REPLY. Otherwise: (1) Read memory/YYYY-MM-DD.md if it exists. (2) Append a new session section with ## Session {HH:MM} containing subsections: Key Events, Knowledge Learned, User Preferences (tag EXPLICIT or INFERRED), Decisions Made, Unfinished. Only record specific, non-trivial information. (3) Promote EXPLICIT entries to MEMORY.md immediately with from:YYYY-MM-DD. INFERRED entries only promote if same pattern in 3+ daily files from last 7 days. Backup MEMORY.md first. Log to memory/.lifecycle.log. (4) If MEMORY.md > 30K chars, compact: delete non-[perm] entries not relevant 60+ days, merge duplicates. Never touch [perm]. Never include credentials.",
          systemPrompt: "Pre-compaction memory flush turn. The session is near auto-compaction; capture durable memories to memory/YYYY-MM-DD.md and promote important entries to MEMORY.md."
        }
      }
    }
  }
}
```

Notes:
- `softThresholdTokens`: flush fires when `totalTokens >= contextWindow - reserveTokensFloor - softThresholdTokens`
- Default `reserveTokensFloor` is 20000 (from platform defaults)
- One flush per compaction cycle (tracked in `sessions.json`)
- Skipped if workspace is read-only or sandboxed
- `NO_REPLY` ensures the flush turn is invisible to the user
