# Post-Review Adversarial Fix Planning

**Problem:** Code review produces N findings. Before writing code, you need a validated fix plan that prioritizes correctly, respects dependency order, and doesn't miss interactions between fixes.

**Pattern:** Apply the same adversarial pipeline to **planning** as to code review: two independent models each produce a fix plan, then cross-review synthesizes the final plan.

## Workflow

```
Review findings → Spec each model → Plans A & B → Cross-review → Synthesis → Final plan
                       │                      │
                  Codex or GLM or Claude   Complementary model
```

### Step 1: Prepare the spec

Write a concise spec describing each finding with:
- Severity (blocker/major/minor)
- Exact file + line
- The root cause (not the symptom)
- The fix approach (1-2 sentences)

Include the format requirements: "each task = 2-5 minutes, one file at a time, exact code, build/test commands, commit message."

### Step 2: Generate plans independently

Dispatch two models in parallel via background terminal:

```bash
# Model A: Codex
cd /path/to/project
codex exec --skip-git-repo-check --sandbox danger-full-access < plan-spec-a.txt

# Model B: GLM-5.2 (pi) or Claude tmux
pi -p --provider zai --model glm-5.2 < plan-spec-b.txt
```

Each model writes its plan to a file (e.g. PLAN_CODEX.md, PLAN_GLM.md).

### Step 3: Cross-review both plans

Compare on these axes:

| Criteria | What to check |
|----------|---------------|
| **Order** | Are blockers first? Does protocol split precede server changes? |
| **Coverage** | Are all findings addressed? If not, which are intentionally deferred? |
| **Test strategy** | Are regression tests included per phase? |
| **Code correctness** | Would the proposed code actually compile and fix the issue? |
| **Dependency model** | spawn_blocking vs per-op connections? authenticated:bool vs string check? |

### Step 4: Resolve divergences

For each divergence between the two plans, decide:

1. **Identify the two positions** (e.g. "Model A uses `authenticated:bool`, Model B checks `login == 'anonymous'`")
2. **Assess tradeoffs** — clarity vs simplicity, correctness vs conciseness, future-proofing vs YAGNI
3. **Pick one** with explicit technical justification
4. **Document the rationale** so future sessions don't re-debate it

### Step 5: Produce synthesis document

Output: a single markdown file containing:
- Comparison table (structure, coverage, approach differences)
- Consensus points (where both models agreed)
- Divergences (each with the two positions + resolution)
- Final merged plan with phase structure

## Validated Example: Chatter Rust Project (2026-07-06)

**Context:** WebSocket chat client/server, 3 crates, ~1500 LOC, 20 adversarial review findings (3 blockers, 10 majors, 7 minors).

**Models used:**
- Codex (Architect) → PLAN_CODEX.md (1414 lines, 4 phases)
- GLM-5.2 via pi (Architect) → PLAN_GLM.md (944 lines, 3 phases)

**Cross-review results:**
- **6 points of consensus** (order, login removal, INSERT fix, deadlock fix, typed auth, server-derived identity)
- **6 points of divergence** resolved:
  1. `authenticated: bool` (GLM) > login string check (Codex)
  2. `LoginOk` (Codex) > `Welcome` (GLM) — clearer semantics
  3. Per-op connections (Codex) > shared Mutex wrapper (GLM) — better scalability
  4. 4-phase structure (Codex) > 3-phase (GLM) — cleaner separation
  5. `NotAuthenticated` variant (GLM) > generic `Error` (Codex) — type-safe
  6. Include minors (Codex) in Phase 5 optional > defer entirely (GLM)

**Timing:** ~6 min total (Codex ~3 min, GLM ~5 min but writing output at 3min+)

## Pitfalls

1. **GLM-5.2 via pi can be slow** (>5 min) on large/general prompts. It writes progressively to disk while running. Don't kill the process — check the output file while it's still running.
2. **Both models may miss the same finding** if the spec is ambiguous. Be explicit about what must be covered.
3. **Different models produce different granularity.** Codex writes more code-per-task; GLM writes more explanation-per-task. The synthesis should pick the right balance.
4. **The cross-review is the most valuable part.** The two independently-produced plans will have different blind spots. A single-model plan is always weaker than the synthesized result.
5. **User trust matters.** When the user says they don't trust GLM or Codex for actual code execution, the adversarial plan provides a validated blueprint that a human (or the trusted model) can follow.
6. **Model pairing diversity matters** — different pairings (Codex+GLM, Claude+Codex, Claude+GLM) surface different tradeoffs. Document which pairing was used so future sessions can compare.
