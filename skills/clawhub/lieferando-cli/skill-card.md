## Description: <br>
Read-only German food-delivery discovery for Lieferando and Uber Eats that lets agents search restaurants near an address, inspect menus, item option groups, prices, delivery fees, ETA, and opening state, while returning JSON envelopes and not supporting login, ordering, or payment. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[karimqpn](https://clawhub.ai/user/karimqpn) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and agents use this skill to discover German food-delivery options, compare restaurants, inspect menus and item options, and prepare a local cost estimate before the user orders directly in the provider app or website. <br>

### Deployment Geography for Use: <br>
Germany <br>

## Known Risks and Mitigations: <br>
Risk: Sensitive home, work, or other address details may be sent to geocoding and food-delivery services or cached locally. <br>
Mitigation: Prefer postcode-only lookups when possible, avoid entering sensitive addresses, and clear local cache or state files when location history should not persist. <br>
Risk: Local cart simulation and pacing data can leave food choices, restaurant slugs, or lookup state under the user home directory. <br>
Mitigation: Treat cart output as a local estimate only, clear the simulated cart after use, and review local state retention before shared or managed deployments. <br>
Risk: Upstream services may rate-limit or block protected endpoints, especially detailed Uber Eats item lookups. <br>
Mitigation: Respect LFD_RATE_LIMITED and LFD_BLOCKED responses, avoid tight retry loops, and use broader search, restaurant, or menu commands when item detail is blocked. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/karimqpn/skills/lieferando-cli) <br>
- [Skill homepage](https://clawhub.ai/skills/lieferando-cli) <br>
- [OpenStreetMap Nominatim search API](https://nominatim.openstreetmap.org/search) <br>


## Skill Output: <br>
**Output Type(s):** [shell commands, JSON, guidance] <br>
**Output Format:** [JSON envelopes from the CLI, with human-facing summaries and guidance derived from those results.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Prices are integer euro cents; failures include machine-readable error codes and retryability.] <br>

## Skill Version(s): <br>
0.2.4 (source: server-resolved release metadata and CLI envelope) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
