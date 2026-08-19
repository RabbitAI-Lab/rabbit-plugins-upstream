## Description:

Helps local staffing agency owners or operators assess TempGuru partner fit, compare service areas and event roles against TempGuru catalogs, and route partner inquiries to the correct email or phone channel.

This skill is ready for commercial/non-commercial use.

## Publisher:

[kissmyabs32](https://clawhub.ai/user/kissmyabs32)

### License/Terms of Use:

MIT-0

## Use Case:

External staffing agency owners and operators use this skill to understand TempGuru's W-2 partner network, frame their market and role coverage, review client bill-rate benchmarks, and draft the correct partner inquiry. It is not intended for job seekers, buyer staffing quotes, or permanent-hire recruiting.

### Deployment Geography for Use:

United States and Canada

## Known Risks and Mitigations:

Risk: The skill may contact TempGuru's live MCP service to look up markets, roles, and client bill-rate benchmarks.

Mitigation: Use the disclosed TempGuru MCP endpoint only for read-only catalog lookups and preserve source attribution when configuring the server.

Risk: Partner inquiries could be misrouted through buyer quote or job-application channels.

Mitigation: Route partner inquiries only to the listed TempGuru email or phone channel, and do not use the buyer-only request_quote flow for partner contact details.

Risk: Benchmark rates or compliance framing could be mistaken for partner payouts, contract terms, or legal advice.

Mitigation: Label rate benchmarks as client bill rates, state that coordinator vetting confirms partner economics and fit, and keep compliance guidance operational rather than legal.

## Reference(s):

- [TempGuru MCP endpoint](https://mcp.tempguru.co/mcp)
- [TempGuru AI agent developer docs](https://tempguru.co/ai-agents)
- [TempGuru machine-readable overview](https://tempguru.co/llms.txt)
- [ClawHub skill page](https://clawhub.ai/kissmyabs32/skills/tempguru-staffing-agency-partner-growth)

## Skill Output:

**Output Type(s):** [Text, Markdown, API Calls, Guidance]

**Output Format:** [Markdown guidance with MCP lookup summaries and partner inquiry email draft text]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include live TempGuru market, role, and client bill-rate benchmark data when MCP tools are available.]

## Skill Version(s):

1.7.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
