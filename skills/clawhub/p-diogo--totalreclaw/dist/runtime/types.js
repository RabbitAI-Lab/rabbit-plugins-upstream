// ---------------------------------------------------------------------------
// Shared plugin runtime types
// ---------------------------------------------------------------------------
//
// Extracted from index.ts so the composing entry point AND the domain modules
// carved out of it (runtime/format-helpers, import/import-runtime, …) can share
// one definition of the OpenClaw plugin-API surface and the internal row shapes
// without a circular import back through index.ts.
//
// Nothing here reads the environment or performs I/O — pure type declarations.
export {};
