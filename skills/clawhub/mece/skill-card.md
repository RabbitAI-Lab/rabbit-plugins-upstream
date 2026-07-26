## Description: <br>
MECE helps an agent decompose large, messy problems into mutually exclusive and collectively exhaustive branches, test for overlaps and gaps, and identify a load-bearing path to action. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[deciqai](https://clawhub.ai/user/deciqai) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Employees, external users, and strategy or product teams use this skill to structure complex analysis, planning, and decision problems into non-overlapping, gap-free branches. It is best suited for messy option lists, issue trees, market strategy, or presentations that need a defensible decomposition. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill may activate during broad planning or strategy discussions where the user is still intentionally brainstorming. <br>
Mitigation: Check whether the user needs structure now; defer MECE decomposition during early creative exploration or trivial decisions. <br>
Risk: A decomposition can appear complete while still using the wrong top-level dimension or hiding overlap in an 'other' branch. <br>
Mitigation: Run explicit mutual-exclusivity, collective-exhaustiveness, and sum-to-whole checks, and compare at least one alternative decomposition dimension. <br>
Risk: Worked examples include historical and market references that may be unsuitable as current evidence without review. <br>
Mitigation: Treat examples as method demonstrations and verify external facts before using them in business decisions. <br>


## Reference(s): <br>
- [Sources - mece](artifact/references/sources.md) <br>
- [Lou Gerstner's IBM Turnaround Decomposition (1993)](artifact/examples/lou-gerstner-ibm-turnaround-decomposition-1993.md) <br>
- [Structuring an AI-Stack Market Strategy MECE (2024-2026)](artifact/examples/ai-stack-market-strategy-decomposition-2024-2026.md) <br>
- [IBM Investor Relations](https://www.ibm.com/investor/) <br>
- [NVIDIA Investor Relations](https://investor.nvidia.com/) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, guidance] <br>
**Output Format:** [Markdown analysis with structured headings] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include step-by-step coaching questions when the user needs help defining the problem.] <br>

## Skill Version(s): <br>
1.0.5 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
