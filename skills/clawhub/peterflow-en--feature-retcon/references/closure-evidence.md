# Closure evidence

For a completed round read the authoritative artifacts and actual results. Check target assertions, stage gates, unexplained residuals, accurate progress and zero remaining work. A blocked environment or skipped necessary check prevents closure.

Write a separate evidence JSON in an authorized local location. It is control data alongside the contract, outside the target journal. Evidence files must exist, be nonempty and be independent of this JSON and the contract. Use the actual round ID and absolute paths without line numbers or anchors. Multiple checks may reuse an adequate report. Provide the detailed commands, outcomes, sections and limitations in the cited material.

```json
{
  "round_id": "id-from-contract",
  "outcome": "completed",
  "completed_stage": "implementation",
  "remaining_work": [],
  "checks": {
    "requirements": {"result": "pass", "evidence": ["/project/verification/retcon.md"]},
    "design": {"result": "pass", "evidence": ["/project/verification/retcon.md"]},
    "tasks": {"result": "pass", "evidence": ["/project/verification/retcon.md"]},
    "implementation": {"result": "pass", "evidence": ["/project/verification/retcon.md"]},
    "residuals": {"result": "pass", "evidence": ["/project/verification/retcon.md"]},
    "watermark": {"result": "pass", "evidence": ["/project/verification/retcon.md"]},
    "absorption": {"result": "pass", "evidence": ["/project/verification/retcon.md"]}
  }
}
```

Include all stages through the completion stage. For every normal close include `residuals` (all lexical and behavioral hits explained), `watermark` (progress matches current state) and `absorption` (all live assertions belong to authoritative artifacts and trace to the endpoint).

For an authorized undo, run `restore`, then verify the actual baseline and active references. Set `outcome` to `restored`, omit `completed_stage` and use checks `baseline`, `references` and `absorption`. Account for any live content unique to the contract.

Run `verify --mark-ready --evidence <json>` followed by `close <contract> --archive <archive>`. If inputs change in between, reverify. Choose a fresh private archive path in an authorized existing directory. On failure inspect `issues` and `closure_issues`. Archive existence alone is insufficient to declare success. Keep exact preimages and archives local with mode 0600 and outside Git. A restored round gets its own archive so the original completed archive survives.
