# Document Release Desk

Version 3.0.0. Requires Python >=3.10.

The complete operations are under operations/upstream and operations/downstream.
Each directory retains its original entry point, implementation, validation,
configuration, examples, source map, dependency declaration and file manifest.
Their component version is 1.1.0; the enclosing package version is 3.0.0.

Run the commands in SKILL.md from this directory with --stage selected explicitly.
The upstream output can be provided to downstream in its declared input field.
The downstream operation requires --output-dir and writes the same local files
as its component implementation. Calls use the caller working directory.
Configured local records remain in the operation modules. No network service
is contacted. A local queue or draft does not confirm an external action.
On Windows choose a short absolute output path to avoid filesystem/SQLite
path-length limits. The root runner forwards output and exit status.
