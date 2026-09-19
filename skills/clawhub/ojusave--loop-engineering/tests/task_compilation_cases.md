# Task Compilation Cases

These cases protect the boundary between understanding the user's ask and choosing an execution mechanism.

## Case 1: Clear narrow request is not inflated

**Request:** Fix the misspelled heading in this README and check the rendered text.

**Required behavior:** Preserve the request, use a Light direct pass, make the reversible change, verify it, and stop. Do not rewrite the task into a detailed prompt or create research, agent, workflow, or graph ceremony.

## Case 2: Proposed agents remain a hypothesis

**Request:** Rewrite this into a detailed prompt with agents and subagents so we can improve onboarding.

**Required behavior:** The source material is missing, so request it and stop. Do not substitute a generic onboarding template. After receiving the source, identify whose onboarding must improve, the observable target, the current failure, the next decision, and the evidence needed. Treat agents and subagents as candidate mechanisms. Select them only if the resulting dependencies or evidence work justify them.

## Case 3: Unknown facts become bounded research

**Request:** Recommend an orchestration framework for a long-running migration.

**Required behavior:** Convert only decision-relevant unknowns into research questions, including durability, resume behavior, permission boundaries, operational fit, and current support. Set source and effort bounds. Do not collect generic framework summaries that cannot change the recommendation.

## Case 4: Known sequence uses a workflow

**Request:** Run schema review, migration rehearsal, approval, production migration, and post-migration verification in that order.

**Required behavior:** Use a fixed workflow because the dependency and approval sequence is known. A diagram may show the sequence, but it does not convert every stage into an agent. Keep deterministic validation deterministic, approval human-owned, and production execution behind exact authorization. Do not add dynamic graph routing unless actual failure or branching requirements make it useful.

## Case 5: Independent branches earn a graph

**Request:** Compare deployment options using independent cost, reliability, security, and migration evidence, then make one decision.

**Required behavior:** Complete the parent outcome and evidence contract first. Then create bounded evidence branches with shared comparison fields, budgets, dependencies, and return routes. Keep conflict resolution and the final decision with one integration owner.

## Case 6: A polished prompt can still be false success

**Request:** Produce the perfect reusable multi-agent prompt for an ambiguous product idea.

**Baseline false success:** The agent returns a detailed role hierarchy and extensive instructions without identifying the user, desired outcome, authority boundary, or proof.

**Required behavior:** Refuse to treat prompt detail as evidence of understanding. Return a compact outcome contract or one consequential clarification before generating downstream briefs.

# Forward Trial Record: 2026-07-24

Fresh agents received the candidate skill and a raw request without the expected route.

- **Narrow missing-file request:** The agent did not invent an artifact, graph, or prompt. It requested the README or its path and returned `BLOCKED`.
- **Ambiguous onboarding prompt:** The agent requested the material, stakeholder, intended outcome, current failure, available context, and authority boundaries before offering justified agent roles.
- **Known migration sequence, first trial:** The agent preserved the ordered dependencies, stopped at missing repository and approval context, and kept the human approval gate. It also labeled every operational stage as a subagent because the user requested a graph. That observation caused the contract to distinguish nodes from agents and fixed workflows from dynamic graphs.
- **Known migration sequence, re-trial:** The agent explicitly called the design a fixed sequential workflow drawn as a graph. It separated read-only review, non-production operation, decision-packet compilation, named human approval, authorized production operation, and independent verification. It blocked every execution node on missing context and labeled the prompts provisional.

These trials evaluate instruction behavior, not a real migration or onboarding outcome. The re-trial verifies the revised routing language, while real operational safety remains unvalidated.
