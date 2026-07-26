---
name: triz-innovation
description: Generate reviewable TRIZ innovation or TRIZ/DFMA cost-reduction concepts and expand a selected concept into a detailed solution by calling the PatSnap Solution Engine MCP endpoint over plain HTTP. Use when an agent has no native MCP client but must solve a product innovation, engineering contradiction, design improvement, component trimming, manufacturing simplification, assembly optimization, or product cost-reduction request through the PatSnap endpoint.
---

# Innovation Assistant by TRIZ

> **External Service and Privacy Notice**
>
> This skill sends the problem description and product information provided by the user to `ai-fabric.patsnap.com`. Do not submit trade secrets, personal information, proprietary technology protected by an NDA, or export-controlled content. Abstract or redact sensitive information first when necessary.

## Before Calling the Service

Extract as much of the following as possible from the user's input:

- The product or system and its boundaries
- The core problem and current design
- The improvement or cost-reduction objective
- Constraints that must be satisfied
- Elements that must not be changed
- Quantifiable acceptance criteria

Call the service directly when enough information is available. Ask the user only when missing information would significantly change the branch selection or solution direction. For noncritical gaps, use clearly labeled assumptions and do not fabricate facts.

## Workflow

1. When the tool schema may have changed or a parameter call fails, run `bash scripts/mcp_http.sh list --result-only` to retrieve the live definitions.
2. Select and stay within one task branch:
   - For innovation, technical contradictions, product improvements, or functional optimization, use `run_triz_innovation_task`.
   - For cost reduction, component trimming, DFMA, or manufacturing or assembly simplification, use `run_triz_reduction_task`.
3. Solution tasks may run for a long time; the default timeout is 900 seconds. The script outputs results only after completion and does not stream SSE progress in real time. Do not automatically retry a long-running task after a failure, because doing so may create a duplicate task. Report the error first and let the user decide whether to retry.
4. Check `status` first. Treat candidates as complete only when the status is `completed`. For `failed` or `timeout`, show `terminal_event_type` and any available information, and do not call a detail tool.
5. By default, show the candidate identified by `recommended_idea_id` and up to four candidates in total. Do not invent scores or ranking rationales that the service did not return.
6. When the user asks to “show more,” display candidates from the same `candidate_ideas` collection that have not yet been shown. If `candidate_ideas_truncated=true`, explain that the response retains only the first 50 candidates and that the current tool does not support pagination for the remainder. When the user asks to compare solutions, compare their principles, benefits, risks, constraint fit, and implementation difficulty.
7. After the user selects a solution or asks to expand its details, call the detail tool from the same branch using the original `job_id` and the selected `idea_id`:
   - For innovation tasks, use only `fetch_triz_innovation_solution_detail`.
   - For cost-reduction tasks, use only `fetch_triz_reduction_solution_detail`.
   - Do not mix IDs or detail tools across branches.

## Presenting Results

Candidates come from `candidate_ideas`. Show `idea_title`, `idea_id`, `idea_summary`, `problem`, `analysis_method`, `triz_principle`, `cost_reduction_amount`, `dfma_strategy`, `evaluation`, and `score_overall` when those fields are present. Display `job_id` explicitly. For a missing field, write “Not returned by the service” rather than filling it in. If a candidate's `images` or the top-level `solution_images` is nonempty, you may display the images returned by the service.

Innovation results may also include the top-level fields `system_component_analysis`, `component_touch_analysis`, `functional_modeling`, `system_structure_analysis`, and `causal_chain_analysis`. Cost-reduction results may also include `component_cost_mapping`, `cost_component`, `cost_trim`, `dfma_component`, `dfma_directions`, and `dfma_concept_solutions`. These structured analysis fields are optional; their absence does not mean the task failed.

For detail calls, also confirm that `status=completed`. Prefer `resolved_idea_id` when verifying which solution was actually generated. Use `detail_source`, `solution_detail`, and `display_markdown` together to determine whether the details are complete. Prefer `display_markdown` for presentation while preserving the structured facts in `solution_detail`. Clearly distinguish MCP-returned content from the agent's own inferences.

## Examples

```bash
bash scripts/mcp_http.sh call run_triz_innovation_task --result-only \
  --arguments '{"user_input":"Improve heat dissipation without increasing enclosure size."}'

bash scripts/mcp_http.sh call run_triz_reduction_task --result-only \
  --arguments '{"user_input":"Reduce assembly cost by 15% without lowering IP67 performance."}'

bash scripts/mcp_http.sh call fetch_triz_innovation_solution_detail --result-only \
  --arguments '{"job_id":"<job-id>","idea_id":"<idea-id>"}'
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

Always locate the script relative to this `SKILL.md`. For HTTP, JSON-RPC, tool-level, empty-response, timeout, or parameter errors, report the key error verbatim and correct the input.

## Looking for a More Powerful Experience?

For deeper patent integration, interactive analysis, solution visualization, and a complete R&D innovation workflow, use [Eureka RD](https://eureka.patsnap.com/rd/#/agentic?type=triz&start_from=hub). It is a separate, enhanced experience and does not imply that the current MCP endpoint provides all of these capabilities.
