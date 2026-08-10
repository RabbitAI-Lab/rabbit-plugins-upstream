---
name: social-persona-profiling
description: >
  Profile people from social-media traces — avatar, profile/cover background, nickname,
  privacy/visibility settings, chat behavior, shared content, self-reported labels — across
  platforms (WeChat, WhatsApp, Instagram, LinkedIn, Telegram, X) and cultures, and deliver an
  honest, evidence-weighted persona read, relationship analysis, or "what should I do next"
  guidance. Built for anyone sizing up a colleague, date, friend, or stranger from limited
  online signals. Capabilities: Big Five (OCEAN) trait estimation, self-presentation &
  self-monitoring (Goffman/Snyder), Higgins self-discrepancy, defense mechanisms (Vaillant),
  attachment and burnout signals, three-layer persona mapping (public persona / private self /
  self-reported), relationship-crisis attribution, and exploratory non-directive next-step discussion by
  scenario (workplace / dating / friendship / scam detection). Safeguards: three-tier
  confidence grading (objective fact / behavioral inference / working hypothesis), moderator
  adjustment for age, culture (individualist vs collectivist), platform, personality baseline
  and digital-native generation, projection-symmetry check, and a Barnum-effect filter that
  deletes any statement true of anyone. Use it when someone asks: "what does this profile
  picture say about them", "analyze this person's personality", "is this person trustworthy",
  "should I get closer to this coworker", "what should I do about this relationship", "is
  this a scam".
  中文摘要：基于社交痕迹（头像/profile封面/昵称/可见性/聊天记录/分享内容/自述标签，跨平台跨文化）做人物侧写、关系分析与行动指导。以大五人格为科学主轴，辅以自我呈现/自我监控、Higgins 自我差异、防御机制、依恋、burnout；强制年龄/文化/平台/性格基线/数字化世代调节，三层置信度分级，投射对称性检查与巴纳姆效应过滤。适用于分析头像人格、判断关系状态/危机、评估话语可信度、并给出"接下来该怎么办"的咨询指导（职场/亲密/朋友/防骗）。
description_zh: 社交人格侧写与关系分析
description_en: Social persona profiling
version: "1.0.4"
disable: false
agent_created: true
read_when:
  - "User explicitly provides social profile data (avatar / profile / nickname / bio from WeChat, WhatsApp, Instagram, LinkedIn) and requests a structured personality analysis"
  - "User requests a persona or social profiling analysis of a specific individual they have social traces of"
  - "User asks for a relationship state or crisis analysis with concrete context provided"
  - "User asks whether someone's statement is credible, with the statement and context provided"
  - "User asks whether to deepen a relationship, trust a friend, or spot a potential scam, with a specific situation described"
not_for:
  - "Analyzing public figures, celebrities, or people without reasonable access to their social traces"
  - "Discriminatory, manipulative, or PUA-style profiling purposes"
  - "Making employment, credit, or legal decisions about the analyzed person"
---

# social-persona-profiling

## ⚠️ Privacy & Use Warning (read first)

**This skill produces speculative personality inferences from limited social traces — it is NOT a psychological assessment, NOT a mental-health diagnosis, and NOT suitable for consequential decisions.**

- **Sensitive personal data**: Inputs (avatars, chat logs, shared content) are personal data. Obtain the subject's consent where feasible; do not profile public figures, minors, or people without reasonable access to their traces.
- **False positives are common**: Personality inferences from social traces have low validity. Every output is a working hypothesis, not a fact. Cross-check with direct interaction before acting.
- **Not for consequential decisions**: Do NOT use outputs for hiring, credit, legal, medical, or relationship-ending decisions. The skill provides exploratory discussion points, not directive guidance.
- **Mental-health boundary**: Frameworks referencing depression/anxiety/emotional-distress (e.g. self-discrepancy) are theoretical patterns, NOT diagnoses. If the subject shows distress signs, recommend professional help — do not label or diagnose.
- **Non-directive**: "What should I do next" outputs are exploratory discussion points for the user's own judgment, not instructions to execute.


A methodology for persona profiling and relationship analysis from social-media traces, aiming to be **professional yet actionable** — use scientific frameworks like the Big Five for grounded inference, use moderators to avoid misreading, and use three-tier confidence grading to stay honest. Guard against two failure modes at once: dressing the client's subjective narrative up as objective conclusion (dishonest), and giving Barnum-style one-size-fits-all readings or culture/age-mismatched labels (unprofessional).

## When to use
- User provides a social avatar / profile / chat history (WeChat, WhatsApp, Instagram, LinkedIn, Telegram, etc.) and asks "what's this person's personality?"
- User is in a relationship crisis and wants attribution + how to handle it
- User wants a "persona profile report" or "relationship analysis report"
- Assessing the credibility of a self-description / chat history
- Scenario-based read on people: whether to deepen a work collaboration, advance a relationship, trust a friend, or spot manipulation/scams
- User requests exploratory (non-directive) discussion of possible next steps, with explicit understanding outputs are hypotheses not instructions

## Hard Rules (learn these first, then the steps)

1. **Three-tier confidence grading (mandatory)** — every conclusion must fit one tier:
   - **High (objective fact)**: what the avatar is, what the background shows, verbatim chat quotes — directly observable, no interpretation.
   - **Medium (behavioral inference)**: tendencies inferred from behavior (e.g. "fast replies + voice messages → high trust") — has behavioral evidence but is one of several explanations.
   - **Working hypothesis (theory construction)**: three-layer needs, core contradictions, stress mechanisms, precise Big Five placement, "true inner self" — products of the analytic framework; **to be verified, never a basis for action**.
2. **What the client says is not fact.** The client is both information source and stakeholder; their account carries confirmation bias, self-serving bias, and emotional coloring. Tag the source of any client statement, and question its reliability.
3. **Projection-symmetry check (mandatory)**: if the analyst's description of the subject (e.g. "hard shell, soft core") resembles the analyst's own structure, warn explicitly — you cannot distinguish "genuinely read them" from "projected myself". Downgrade all "inner core" conclusions about the subject by one tier.
4. **The subject is not present and cannot defend themselves.** All attribution about the subject is single-sided; the report must state this power asymmetry.
5. **Present the final analysis, leave no editing traces.** Do critical self-review before producing and fold results into conclusions, but the report body must NOT contain meta-language like "correction:", "clarification", or "my review found". The client wants a clean, deep final judgment, not a self-congratulatory audit trail. Weave methodology caveats (validity ceiling, projection symmetry) into the relevant analysis sections; don't add a separate "audit chapter" to show off.
6. **Must close with a psychological formulation.** Don't stop at behavior listing — give an integrated professional formulation: "what kind of person is this". Integrate self-monitoring / self-discrepancy (Higgins) / self-esteem type (contingent & fragile) / defense mechanisms / attachment / burnout, and give a one-sentence formulation. Note frameworks differ in validity (see toolbox): attachment only as a tendency, never a definitive type; Big Five only at "medium" confidence.
7. **Adjust before interpreting.** Every signal must be calibrated by moderators (age/developmental stage, cultural baseline, personality baseline, digital-native generation) before interpretation. Behavior within the baseline carries no personality signal; only "deviation from baseline" can be a signal.

## Theory Toolbox (quick ref — see @references/psych-frameworks.md)

Ranked by scientific validity. **Theories generate hypotheses to verify, not labels to stick.**

| Framework | Validity | Use & warning |
|---|---|---|
| **Big Five OCEAN** | High (backbone) | The only widely validated personality structure. Social traces → five traits only weakly correlated (r .1–.3); needs long-term multi-context samples; always mark "medium", never "high" |
| **Self-presentation / self-monitoring** (Goffman / Snyder) | Medium-high | An avatar is "the me I want to show", not the real me; first judge whether the subject is a high or low self-monitor to gauge the signal-to-noise ratio of their traces |
| **Self-discrepancy** (Higgins) | Medium-high | Ideal–actual gap → dejection; ought–actual gap → anxiety; large persona–actual gap = emotional-distress risk |
| **Defense mechanisms** (Vaillant) | Medium | Watch the first reaction to setbacks (rationalization / denial / intellectualization / humor); never type someone from a single reaction |
| **burnout** (Maslach) | Medium | Requires exhaustion + cynicism + reduced efficacy together; "tired" alone ≠ burnout |
| **Attachment type** | **Low (use with caution)** | Needs AAI/ECR scales; inferring from avatar/chat has very low validity; working hypothesis only, must be flagged, never definitive |
| **MBTI / astrology** | **Very low** | Social currency / self-labels, not empirical tools; self-reports only reflect "how they want to be seen", never count as Big Five evidence |

## Moderators (read before interpreting — see @references/moderators.md)

The same signal can mean opposite things across groups. **Interpreting without adjusting is the most common error.**

- **Age / developmental stage**: teen anime/idol avatars = normal identity exploration (not "immature"); middle-aged child/scenery avatars = normal life-focus shift (not "hiding the self"). **Avatar information content decreases with age; over-reading older adults' avatars is the most error-prone.**
- **Cultural baseline**: collectivist/high-context cultures (East Asia, Latin America, Middle East) — non-real-person avatars, indirect self-display, restricted visibility are cultural norms, not personal signals; individualist/low-context cultures (North America, Western Europe) — direct real-face display is more common. The same behavior is baseline in one context and a signal in another.
- **Personality baseline**: introverts using non-real avatars and extroverts using real photos are both baselines, not signals. **Read deviation from the personal baseline, not the absolute type.**
- **Digital-native generation**: Gen Z multi-platform multi-persona is the norm; a single-platform image ≠ the whole person. Older users' single-platform real-identity is the norm.
- **Gender / ethnicity**: group-level trends have huge individual variance; beware stereotyping; cross-ethnic comparison is essentially cultural difference — attribute to culture, not ethnicity.

## Application Scenarios & Ethics

- **Scenario split**: workplace collaboration (reliability & boundaries), romantic decisions (attachment & values), friendship trust (consistency), scam detection (inconsistency & manipulation signals) — different scenarios have different decision criteria and risk appetite; confirm the client's scenario first.
- **Client intent screening**: if the profiling aims to manipulate, PUA, deceive, or harm the subject, **refuse**.
- **Prohibited**: never for discriminatory decisions (hiring, credit, insurance, background-check scoring).
- **Subject dignity**: profiling is single-sided; the subject is unaware and cannot defend themselves; results must not leak to third parties or be used for public judgment.

## Steps

> This is a pure LLM analysis task (no deterministic script steps); all steps are `[LLM]`. Architecture: Workflow / Prompt Chaining (sequential steps + the audit checkpoint at step 6).

1. **[LLM] Inventory & classify data**: sort all material into "objective fact / behavior / user-transcribed / self-reported". First confirm what you saw directly (images can be read directly) vs what the user transcribed (transcription loss).
2. **[LLM] Moderator adjustment first**: confirm the subject's age/developmental stage, cultural/subcultural baseline, personality baseline, digital-native generation. Remove "baseline-normal" behavior (carries no personality signal); keep only "deviation from baseline" as candidate signals. See @references/moderators.md.
3. **[LLM] Layered persona**: public persona / private self / self-reported layer. Keep the three separate; don't rush into a "unified narrative". If the subject has a self-reported persona, further split into "constructed persona / self-perception / actual image" and analyze the gaps — persona and actual often run opposite; the size of the self-perception–actual gap is itself a key insight (large gap = low self-awareness or unwillingness to admit).
4. **[LLM] Grade confidence item by item**: three tiers (objective fact / behavioral inference / working hypothesis). Better low than high. Big Five always "medium"; attachment only a working hypothesis.
5. **[LLM] (if a relationship event) Attribution**: reconstruct the timeline, but state it is single-sided. Responsibility assignment must declare "contains self-serving bias".
6. **[LLM] Critical review (mandatory)**: run the bias checklist (below) before producing, and give a "specific over-inference list".
7. **[LLM] Psychological formulation close**: integrate the toolbox into "what kind of person is this" + a one-sentence formulation.
8. **[LLM] Action guidance**: besides the report, give actionable "what to do next". Confirm the client's scenario (workplace / dating / friendship / scam), organize into "do now / observation period / long-term strategy"; advice rests only on dependable facts, working hypotheses only flag what to watch. Templates: @references/consulting-playbook.md.

## Output Format (report skeleton)

Recommended structure, trim as needed:

1. **Data basis**: objective facts (no acquisition-method tags unless data was filtered/transcribed).
2. **Layered persona**: public / private / self-reported; or persona / self-perception / actual. Analyze inter-layer gaps.
3. **Psychological dynamics**: integrate the toolbox, tie each to behavioral evidence.
4. **Psychological formulation**: what kind of person + one-sentence formulation (the core deliverable).
5. **Big Five placement**: five traits, all "medium" confidence.
6. **Action guidance (what to do next)**: by scenario, "do now / observation / long-term" three tiers, resting on dependable facts. Templates: @references/consulting-playbook.md.
7. **Methodology note**: validity ceiling + position statement, brief, at the end.

## Failure Handling

| Scenario | Action |
|------|------|
| Insufficient data (single avatar / single post) | State only very limited inference is possible, refuse a full formulation; suggest multi-context, longitudinal samples |
| Client requests discriminatory / manipulative use | Refuse, state the ethical boundary (see Application Scenarios & Ethics) |
| Cannot confirm subject baseline (age / culture unknown) | Ask the client first; if unavailable, declare "baseline not calibrated, overall confidence downgraded one tier" in the report |
| Inference conflicts with client expectation | Don't bend to expectation; present the evidence-supported conclusion and flag the divergence |
| Material contains identifiable sensitive info | Analyze internally only; don't restate identifiable details in output; remind the client about the subject's privacy |

## Bias Checklist (self-check before producing)
- **Validity ceiling**: social avatar/traces → personality has only weak academic support (Gosling's physical/virtual environment personality expression, cross-cultural collectivist explanations of avatar choice, broad Big Five correspondence research); supports only weak correlation at "broad trait + cultural background" level, not "type → fixed personality" mapping.
- **Confirmation bias**: was the material filtered by the client? Did they only give parts supporting one reading? (only applies if data is filtered/fragmentary; skip if the client states it's a complete conversation flow)
- **Information cascade loss**: analysis → user transcription → user memory/emotion; distortion compounds at each layer. (only when relying on secondhand transcription; not when transcription is factual or images are read directly)
- **Narrator-protagonist effect**: the client narrates, tending to cast themselves as the "clear-eyed observer" and the subject as the "observed object".
- **Self-serving bias**: does attribution happen right after the client's emotional event? Does it assign problems to the subject's "structure" to protect the self?
- **Narrative over-integration**: are independent elements (nickname + avatar + background) forced into one "unified theme"? When elements don't cohere, the so-called "tension aesthetic" is often the analyst's framework imposition.
- **Circular reasoning**: the persona was inferred from these behaviors, then used to explain them — that is consistency checking, not causal explanation.

## Pitfalls
- **Barnum effect (biggest trap)**: vague descriptions feel accurate to everyone ("strong outside, soft inside", "longing to be understood"). Test: would this hold for any random person? If yes = delete it. Every formulation must be specific, differentiating, falsifiable.
- **Attachment labeling**: judging "avoidant/anxious attachment" from avatar/chat has very low validity and needs scales. Working hypothesis only, flagged, never definitive.
- **Clinical-term abuse**: "learned helplessness", "regression", "burnout" have specific meanings; don't use casually. Say "expression of helplessness" not "learned helplessness".
- **Treating MBTI/astrology self-report as measurement**: ENTJ, earth-sign etc. are self-idealizing labels; they only reflect "how they want to be seen", never Big Five evidence.
- **Reading cultural norm as personality**: collectivist-culture users using non-real avatars and restricted visibility (group/time-limited) is common (privacy vigilance + indirect self-display); don't read cultural norm as a personal signal.
- **Romanticizing**: a polite reply ("thanks", "I know") ≠ "trust rising" or "we've seen each other's vulnerability".
- **Over-inferring from one sample**: a "behavior pattern" induced from a single event has n=1; not a confirmed stable pattern.

## Verification
After producing the report, self-check:
- Was moderator adjustment done first (age/culture/personality baseline/digital-native generation), removing "baseline-normal" signals?
- Was the use scenario and client intent confirmed compliant (non-manipulative, non-discriminatory)?
- Does every conclusion carry a confidence tier tag?
- If data was client-filtered/transcribed, was information loss flagged? (skip when data is complete and transcription factual — avoid inapplicable disclaimer noise)
- Was the projection-symmetry check done (if applicable)?
- Is the report body clean — no meta-language like "correction: / clarification / my review found", only final analysis?
- Does it close with a clear psychological formulation (what kind of person + one sentence), not stop at behavior listing?
- Is there a "specific over-inference list" that singles out and downgrades the weakest claims?
- Was the client reminded that the subject cannot defend themselves in this document?
If any answer is "no", the report fails the honesty bar — rework.
