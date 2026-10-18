# Knowledge and capability discovery

`wemol-cli search "topic or task" --channel "channel-name"` searches public documents, modules, and workflows. Results include candidates, descriptions, and matching evidence; interface detail depends on the search intent. `--source all` is the default. Narrow to `module|flow|docs` when the task specifically needs that source; a concept question can benefit from all three.

Use `--intent explain` for concepts and methods, `compare` for comparisons, `execute` to find execution candidates, or `route` for initial exploration. Every search intent is read-only, including `execute`. Use a concise scientific topic or task phrase in the language appropriate to the query; English skill instructions do not require English queries.

## Choose and refine search terms

Search matches text in names, tags, descriptions, and other indexed content; do not assume automatic synonym expansion or translation. Use the scientific object and desired action to choose a precise phrase. A canonical name found in returned evidence is useful for a focused follow-up.

When results are empty, weakly related, or appear to miss the intended capability, try an appropriate synonym, related term, established abbreviation, or Chinese/English equivalent. For example, alternative queries for the same nanobody humanization goal could be `纳米抗体 人源化` and `Nanobody Humanization`; `VHH humanization` may help when VHH is the intended object. Separating Chinese object and action terms can also help when the combined phrase does not match the catalog wording.

- Search useful alternatives separately rather than combining every synonym and language into one long query; extra terms can change matching and ranking. Choose follow-ups from the observed results, not a mandatory sequence of all variants.
- Preserve the user's object, method, version, and input/output constraints while rewording. Related terms can discover candidates but do not establish equivalent methods or interchangeable scientific objects. Make any deliberate broadening explicit.
- Inspect matching evidence and read relevant document text or capability overviews. A phrase mentioned in a description may refer to another capability. Reuse returned references to recognize the same candidate across queries; a missing result in a bounded list does not establish that a capability or version is unavailable.
- Stop reformulating when the evidence is sufficient for the current purpose. If meaningful alternatives still leave a gap, report that gap. Source unavailability, authentication errors, and refresh warnings are not vocabulary problems.

## Explain concepts and methods

Search for evidence relevant to the question, then read the material needed to support the answer:

- For a document hit, use `wemol-cli document --channel "channel-name" --id "returned-document-id"` to read its text.
- For a module or workflow, use its returned `capability` with `--view overview` to understand its purpose. Read a workflow's `--view structure` when its steps and connections help explain the method.
- Read input contracts only when the question requires prerequisites or execution details; concept explanations do not require filling a job template.

Explain the concept using the retrieved evidence and identify the documents or capabilities that support platform-specific claims. If a relevant workflow is found, briefly describe the practical path when it helps answer the question. A search match alone does not prove scientific suitability or readiness to run with the user's data.

Preserve the limitations declared by `warnings` and `coverage`. Distinguish no matches from unavailable sources or failed verification; an empty result does not prove the platform has no relevant information or capability. When evidence remains insufficient, state the gap and distinguish any background explanation from platform evidence.

## Select and understand capabilities

Judge suitability by the scientific object, purpose, and input/output contracts. Similar names, high rank, or compatible file formats do not establish scientific applicability.

When only a name or purpose is known, search to obtain the candidate's `capability`. When that reference is already known, read it directly without searching again. For example, reuse a returned `"capability": "flow:456"` as `--capability "flow:456"`; do not replace it with a display name.

Use `wemol-cli capability --channel "channel-name" --capability "flow:456"` with the view needed for the question (replace the example reference with an actual result):

- Default `inputs`: inputs needed to run with the current configuration; a module with multiple methods may require `--method`.
- `--view overview`: purpose and overview.
- `--view structure`: workflow nodes and connections.
- `--view node --node "node-reference-or-unique-name"`: configurable inputs for one workflow node.

Running a workflow does not require expanding every node's parameters. Read `structure` to understand its composition and the relevant `node` when adjusting local configuration. Use `capabilities` to browse a catalog; searching does not require traversing it.
