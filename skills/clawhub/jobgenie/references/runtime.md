# Five rounds on one Claw, with optional role assignment

## Default: one Claw

Run the complete method on the current OpenClaw using its configured model and available tools. Research, selection, drafting, review and correction are five distinct rounds of work; they do not require five agents, another account or a custom workflow service. Read the corresponding [stage prompt](stage-prompts.md) at each round. Save the useful round outputs in the application's directory so the next round can use them and interrupted work can resume.

When the user wants jobs found first, use [job discovery](job-discovery.md) to read their résumé/matrix, establish missing search preferences and find sourced opportunities. Discovery precedes the selected application's five rounds and can be skipped for a supplied posting. Optional role assignment may name an existing scout; one Claw handles it by default.

Review and correction stay separate. The same Claw can take the review role for round 4 and return to the writer role for round 5. A new isolated review context can help when native task/subagent tools are already available. Lack of those tools does not block the default workflow. Do not claim an independent reviewer ran when the same context performed the review.

## Optional: let the user assign existing bots

No configuration step is needed for the default. When the user wants multiple bots, accept a simple instruction such as:

> This bot writes; that bot reviews.

Save the names and assignments in their existing preferences/feedback record. Writer owns rounds 1, 2, 3 and 5; reviewer owns round 4. If the user prefers different per-round assignments, save those instead. An already available separate model family can provide another perspective, but is optional.

Resolve the named roles using existing reachable agents, sessions or connections. Do not require the user to supply technical IDs or reconfigure servers/providers. If a chosen bot is unavailable or disconnected, report the actual limitation and offer local review or a handoff the user can pass to it. Do not pretend separate installations share files. Send the actual relevant source contents or accessible artifacts with the handoff.

The reviewer receives the JD, OSINT, full career reference, current feedback and actual draft. It judges the documents against the employer's work and the applicant's capabilities, without the selector's conclusions being treated as its verdict. Its single consolidated correction set goes to the writer, who finishes the documents. No additional language-edit, fit, claim, fresh-reader or final-judge stage is added.

## OSINT collection inside round 1

Before isolated research synthesis, the calling Claw uses its existing public web search/fetch/browser tools to gather the actual JD, pay information and role-relevant company material. Pass dated source CONTENT and URLs, not inaccessible paths or just snippets. Reuse applicable sources, record inaccessible information privately and proceed from JD clues when necessary. An isolated synthesis call alone is not OSINT. This collection is inside round 1, not a sixth reasoning stage.

## Documents and delivery

Use available document tools to produce the exact final wording in the requested formats. Google services, Slack and any particular provider are optional. The bundled Python-standard-library DOCX producers preserve the approved baseline layout and support arbitrary HTTPS/Markdown links; they contain no candidate data or credentials. Run:

```sh
python3 {baseDir}/scripts/render_documents.py packet.json output-directory
```

The input uses `resume_blocks`, `cover_letter_lines`, required `contact_lines_count`, and optional unchanged `application_answers`. Résumé block kinds are `name`, `contact`, `headline`, `summary`, `section`, `role_header`, `context`, `achievement`, `publication`, `skills` and `education`; role content has a matching `role_id`. Each block is one paragraph. Letter lines are name, contact lines, date, recipient, salutation, body, closing and signature. The Claw sets `contact_lines_count` to the actual number of contact paragraphs; do not default to two or ask the user for technical setup. Optional `letter_spacing` accepts `standard` or `compact`. Read and apply the [formatting guide](formatting.md), including visible paragraph/section spacing.

Use these producers when their readable baseline fits the user's requested presentation; use an existing suitable document tool when a different format or house style is wanted. PDF export uses the environment's available document/PDF tools. If a requested export is unavailable, report that specific missing capability and provide the usable text/DOCX; do not claim the PDF was created. Do not install system packages or configure an external service merely to run this skill.

File production and affected layout/text checks occur inside drafting/delivery, not as another reasoning/approval stage. Preserve readable fonts, layout, publication/employer association, dates and working links. Compare source wording with the actual documents and inspect rendered pages. Fix clipping, awkward grouping or overflow without quietly weakening the writing. The baseline's specific fonts and the size of one past application are not universal word or page limits.

Preserve outputs and recover a concrete failed operation without replaying successful work. If a document needs a scoped delivery correction, preserve the already-good paired document. Once the user approves the pair, retain that exact revision and JD. Deliver actual requested files and accessible text, not a clearance report.

The packet helper validates both documents before writing, saves the source packet in UTF-8, and publishes complete document files from temporary staging. If a file operation fails, complete the identical saved packet with:

```sh
python3 {baseDir}/scripts/render_documents.py packet.json output-directory --resume
```

This verifies the saved receipts for both documents, preserves existing documents and builds only missing ones. If an existing document has changed or lacks its receipt, preserve the files and use a new revision directory. A changed packet belongs in a new revision directory; never overwrite an approved pair to recover an unrelated operation. No extra checker service is required.

The writing workflow ends after corrected documents. It does not enter employer forms, submit applications, create tracker outcomes, schedule work or alter accounts/models/automations. Preserve existing holds and follow the user's actual submission authorization if they separately request that operation; do not invent repeated approvals.
