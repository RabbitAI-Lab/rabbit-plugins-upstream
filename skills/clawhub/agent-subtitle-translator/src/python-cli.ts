import { execFile } from "node:child_process";
import { readFile } from "node:fs/promises";
import path from "node:path";

export interface SubtitleCommandResult {
  report: Record<string, unknown>;
  stdout: string;
  stderr: string;
}

export class SubtitleCommandError extends Error {
  readonly stderr: string;
  readonly stdout: string;
  readonly command: string[];

  constructor(message: string, command: string[], stdout: string, stderr: string) {
    super(message);
    this.name = "SubtitleCommandError";
    this.stderr = stderr;
    this.stdout = stdout;
    this.command = command;
  }
}

export interface SubtitleCliOptions {
  skillRoot: string;
  pythonCommand?: string;
}

function parseJsonReport(output: string): Record<string, unknown> {
  const trimmed = output.trim();
  if (!trimmed) {
    return {};
  }
  try {
    const parsed: unknown = JSON.parse(trimmed);
    return parsed && typeof parsed === "object" ? (parsed as Record<string, unknown>) : {};
  } catch {
    return {};
  }
}

function errorMessage(stdout: string, stderr: string, fallback: string): string {
  const report = parseJsonReport(stderr) as { error?: unknown };
  if (typeof report.error === "string" && report.error.trim()) {
    return report.error;
  }
  const output = `${stderr}\n${stdout}`.trim();
  return output || fallback;
}

export class SubtitleCli {
  private readonly scriptPath: string;
  private readonly pythonCommand: string;

  constructor(options: SubtitleCliOptions) {
    this.scriptPath = path.join(options.skillRoot, "scripts", "subtitle_tool.py");
    this.pythonCommand = options.pythonCommand ?? "python3";
  }

  private run(args: string[]): Promise<SubtitleCommandResult> {
    const command = [this.scriptPath, ...args];
    return new Promise((resolve, reject) => {
      execFile(
        this.pythonCommand,
        command,
        {
          cwd: path.dirname(this.scriptPath),
          encoding: "utf8",
          maxBuffer: 8 * 1024 * 1024,
        },
        (error, stdout, stderr) => {
          const textOut = String(stdout ?? "");
          const textErr = String(stderr ?? "");
          if (error) {
            reject(
              new SubtitleCommandError(
                errorMessage(textOut, textErr, error.message),
                command,
                textOut,
                textErr,
              ),
            );
            return;
          }
          resolve({ report: parseJsonReport(textOut), stdout: textOut, stderr: textErr });
        },
      );
    });
  }

  prepare(inputPath: string, targetLanguage: string, sourceLanguage: string | undefined, batchSize: number, workDir: string): Promise<SubtitleCommandResult> {
    const args = [
      "prepare",
      inputPath,
      "--target-language",
      targetLanguage,
      "--batch-size",
      String(batchSize),
      "--work-dir",
      workDir,
    ];
    if (sourceLanguage) {
      args.push("--source-language", sourceLanguage);
    }
    return this.run(args);
  }

  validateResponse(
    manifestPath: string,
    batch: number,
    responsePath: string,
    allowStyleFallback: boolean,
  ): Promise<SubtitleCommandResult> {
    const args = [
      "validate-response",
      "--manifest",
      manifestPath,
      "--batch",
      String(batch),
      "--response",
      responsePath,
    ];
    if (allowStyleFallback) {
      args.push("--allow-style-fallback");
    }
    return this.run(args);
  }

  compose(manifestPath: string, outputPath?: string, overwrite = false): Promise<SubtitleCommandResult> {
    const args = ["compose", "--manifest", manifestPath];
    if (outputPath) {
      args.push("--output", outputPath);
    }
    if (overwrite) {
      args.push("--overwrite");
    }
    return this.run(args);
  }

  async readManifest(manifestPath: string): Promise<Record<string, unknown>> {
    const raw = await readFile(manifestPath, "utf8");
    const parsed: unknown = JSON.parse(raw);
    if (!parsed || typeof parsed !== "object") {
      throw new Error(`Manifest is not an object: ${manifestPath}`);
    }
    return parsed as Record<string, unknown>;
  }
}
