# Check both directions

A requirement says selection order is preserved. The design sorts names. Select B then A. The planned export writes A then B. Link the requirement and the sort step. A plan that simply refers to the required order already covers it.

An empty selection must produce a header-only file. A task named “verify export” checks only a nonempty array through a converter. Add the empty-input assertion at the export entry point to the original task.

The header step has a source in the requirement. An “upload to cloud drive” task needs a requirement or a technical dependency of its own. If same-name files have no defined overwrite policy and the choice changes user data, isolate that decision and proceed with the unaffected cases.
