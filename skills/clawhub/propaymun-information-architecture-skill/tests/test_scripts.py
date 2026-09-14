from __future__ import annotations

import json
import re
import subprocess
import sys
import tempfile
import unittest
import zipfile
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = ROOT / "scripts"
FIXTURES = ROOT / "tests" / "fixtures"
PACKAGES = ROOT / "packages"
sys.path.insert(0, str(SCRIPTS))

from validate_eval_cases import validate_data


class SkillScriptTests(unittest.TestCase):
    def run_script(self, name: str, *args: str) -> subprocess.CompletedProcess[str]:
        return subprocess.run(
            [sys.executable, str(SCRIPTS / name), *args],
            cwd=ROOT,
            text=True,
            capture_output=True,
            check=False,
        )

    def test_valid_semantic_ia_2_model_passes(self) -> None:
        result = self.run_script("validate_ia_model.py", str(FIXTURES / "valid-semantic-ia.json"), "--json")
        self.assertEqual(result.returncode, 0, result.stderr or result.stdout)
        payload = json.loads(result.stdout)
        self.assertTrue(payload["valid"])
        self.assertEqual(payload["errors"], [])

    def test_invalid_model_fails_with_structural_errors(self) -> None:
        result = self.run_script("validate_ia_model.py", str(FIXTURES / "invalid-semantic-ia.json"), "--json")
        self.assertEqual(result.returncode, 1)
        payload = json.loads(result.stdout)
        self.assertFalse(payload["valid"])
        self.assertTrue(any("model_version" in error for error in payload["errors"]))
        self.assertTrue(any("missing domain" in error for error in payload["errors"]))
        self.assertTrue(any("blocking unknown" in error for error in payload["errors"]))

    def test_valid_companion_models_pass(self) -> None:
        for filename in ("valid-product-sitemap.json", "valid-user-flow.json"):
            with self.subTest(filename=filename):
                result = self.run_script("validate_companion_model.py", str(FIXTURES / filename), "--json")
                self.assertEqual(result.returncode, 0, result.stderr or result.stdout)
                payload = json.loads(result.stdout)
                self.assertTrue(payload["valid"])
                self.assertEqual(payload["errors"], [])

    def test_invalid_companion_models_fail_with_semantic_errors(self) -> None:
        sitemap = self.run_script("validate_companion_model.py", str(FIXTURES / "invalid-product-sitemap.json"), "--json")
        self.assertEqual(sitemap.returncode, 1)
        sitemap_payload = json.loads(sitemap.stdout)
        self.assertTrue(any("cycle" in error for error in sitemap_payload["errors"]))
        self.assertTrue(any("missing to destination" in error for error in sitemap_payload["errors"]))
        self.assertTrue(any("semantic_refs" in error for error in sitemap_payload["errors"]))
        self.assertTrue(any("destination_kind" in error for error in sitemap_payload["errors"]))

        flow = self.run_script("validate_companion_model.py", str(FIXTURES / "invalid-user-flow.json"), "--json")
        self.assertEqual(flow.returncode, 1)
        flow_payload = json.loads(flow.stdout)
        self.assertTrue(any("at least two outgoing" in error for error in flow_payload["errors"]))
        self.assertTrue(any("recovery transition" in error for error in flow_payload["errors"]))
        self.assertTrue(any("unreachable" in error for error in flow_payload["errors"]))
        self.assertTrue(any("label every outgoing condition" in error for error in flow_payload["errors"]))

    def test_every_item_requires_an_existing_domain(self) -> None:
        data = json.loads((FIXTURES / "valid-semantic-ia.json").read_text(encoding="utf-8"))
        data["items"][0]["domain_id"] = "missing-domain"
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "invalid-domain.json"
            path.write_text(json.dumps(data), encoding="utf-8")
            result = self.run_script("validate_ia_model.py", str(path), "--json")
        self.assertEqual(result.returncode, 1)
        self.assertIn("missing domain", result.stdout)

    def test_html_renderer_exposes_domains_hierarchy_and_relationships(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            output = Path(directory) / "ia.html"
            result = self.run_script("render_ia_html.py", str(FIXTURES / "valid-semantic-ia.json"), "-o", str(output))
            self.assertEqual(result.returncode, 0, result.stderr or result.stdout)
            rendered = output.read_text(encoding="utf-8")
            self.assertIn('<html lang="en" dir="ltr">', rendered)
            self.assertIn("Team Knowledge Product", rendered)
            self.assertIn("Information domains", rendered)
            self.assertIn("People and access", rendered)
            self.assertIn("Projects reference working documents", rendered)
            self.assertIn("Information structure", rendered)
            self.assertIn("Priority information needs", rendered)
            self.assertIn("Roles and access", rendered)
            self.assertIn("Lifecycles", rendered)

    def test_validator_rejects_empty_or_semantically_invalid_models(self) -> None:
        data = json.loads((FIXTURES / "valid-semantic-ia.json").read_text(encoding="utf-8"))
        data["domains"] = []
        data["items"] = []
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "empty.json"
            path.write_text(json.dumps(data), encoding="utf-8")
            result = self.run_script("validate_ia_model.py", str(path), "--json")
        self.assertEqual(result.returncode, 1)
        self.assertIn("at least one information domain", result.stdout)
        self.assertIn("at least one item", result.stdout)

        data = json.loads((FIXTURES / "valid-semantic-ia.json").read_text(encoding="utf-8"))
        data["items"][0]["kind"] = "screen"
        data["permissions"][0]["scope"] = ""
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "invalid-semantics.json"
            path.write_text(json.dumps(data), encoding="utf-8")
            result = self.run_script("validate_ia_model.py", str(path), "--json")
        self.assertEqual(result.returncode, 1)
        self.assertIn("kind must be one of", result.stdout)
        self.assertIn("scope must be a non-empty string", result.stdout)

    def test_workspace_kit_is_self_contained(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            workspace = Path(directory) / "workspace.md"
            agent_zip = Path(directory) / "agent.zip"
            result = self.run_script(
                "build_packages.py",
                "--root", str(ROOT),
                "--workspace-output", str(workspace),
                "--agent-output", str(agent_zip),
                "--skip-legacy-aliases",
            )
            self.assertEqual(result.returncode, 0, result.stderr or result.stdout)
            packaged = workspace.read_text(encoding="utf-8")
            self.assertIn("ProPaymun IA Workspace Kit", packaged)
            self.assertIn("adaptive sufficiency loop", packaged.lower())
            self.assertIn("> Embedded source: references/localization.md", packaged)
            self.assertIn("> Embedded source: references/sitemap.md", packaged)
            self.assertIn("> Embedded source: references/user-flow.md", packaged)
            self.assertIn("> Embedded source: references/visual-builder-handoff.md", packaged)
            self.assertIn("short copy-ready launch instruction", packaged)
            self.assertNotIn("](references/", packaged)

    def test_generated_packages_and_legacy_aliases_are_current(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            workspace = Path(directory) / "workspace.md"
            agent_zip = Path(directory) / "agent.zip"
            result = self.run_script(
                "build_packages.py",
                "--root", str(ROOT),
                "--workspace-output", str(workspace),
                "--agent-output", str(agent_zip),
                "--skip-legacy-aliases",
            )
            self.assertEqual(result.returncode, 0, result.stderr or result.stdout)
            canonical_workspace = PACKAGES / "workspace-kit" / "propaymun-ia-workspace-kit.md"
            canonical_agent = PACKAGES / "agent-skill" / "propaymun-information-architecture.zip"
            self.assertEqual(workspace.read_bytes(), canonical_workspace.read_bytes())
            self.assertEqual(agent_zip.read_bytes(), canonical_agent.read_bytes())
            self.assertEqual(canonical_workspace.read_bytes(), (ROOT / "install" / "universal-web" / "propaymun-information-architecture.md").read_bytes())
            self.assertEqual(canonical_agent.read_bytes(), (ROOT / "install" / "claude-ai" / "propaymun-information-architecture.zip").read_bytes())
            self.assertEqual(
                (PACKAGES / "workspace-kit" / "WORKSPACE_INSTRUCTIONS.md").read_bytes(),
                (ROOT / "install" / "universal-web" / "PROJECT_INSTRUCTIONS.md").read_bytes(),
            )

    def test_agent_skill_package_has_canonical_resources(self) -> None:
        archive_path = PACKAGES / "agent-skill" / "propaymun-information-architecture.zip"
        with zipfile.ZipFile(archive_path) as archive:
            names = set(archive.namelist())
            base = "propaymun-information-architecture/"
            self.assertIn(base + "SKILL.md", names)
            self.assertIn(base + "references/discovery.md", names)
            self.assertIn(base + "references/localization.md", names)
            self.assertIn(base + "references/sitemap.md", names)
            self.assertIn(base + "references/user-flow.md", names)
            self.assertIn(base + "references/visual-builder-handoff.md", names)
            self.assertIn(base + "schema/semantic-ia.schema.json", names)
            self.assertIn(base + "schema/product-sitemap.schema.json", names)
            self.assertIn(base + "schema/user-flow.schema.json", names)
            self.assertIn(base + "scripts/validate_companion_model.py", names)
            self.assertIn(base + "scripts/export_builder_handoff.py", names)
            self.assertNotIn(base + "tests/test_scripts.py", names)

    def test_visual_builder_handoff_outputs_spec_and_launch_text(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            specification = Path(directory) / "build-spec.md"
            launch = Path(directory) / "launch.txt"
            result = self.run_script(
                "export_builder_handoff.py",
                str(FIXTURES / "valid-semantic-ia.json"),
                "--target", "figma-make",
                "-o", str(specification),
                "--launch-output", str(launch),
            )
            self.assertEqual(result.returncode, 0, result.stderr or result.stdout)
            prompt = specification.read_text(encoding="utf-8")
            launch_text = launch.read_text(encoding="utf-8")
            self.assertIn("Build a Connected Information Architecture Blueprint", prompt)
            self.assertIn("IA Reference Lock", prompt)
            self.assertIn("semantic drift", prompt)
            self.assertIn("Domain-to-item map", prompt)
            self.assertIn("Projects reference working documents", prompt)
            self.assertIn("at least about two-thirds", prompt)
            self.assertIn("Do not create a sitemap, user flow", prompt)
            self.assertNotIn("Review Explorer", prompt)
            self.assertLess(len(launch_text.strip()), 240)
            self.assertIn("attached Markdown file", launch_text)

    def test_not_ready_model_cannot_export(self) -> None:
        data = json.loads((FIXTURES / "valid-semantic-ia.json").read_text(encoding="utf-8"))
        data["meta"]["handoff"]["readiness"] = "not-ready"
        with tempfile.TemporaryDirectory() as directory:
            model = Path(directory) / "not-ready.json"
            model.write_text(json.dumps(data), encoding="utf-8")
            result = self.run_script("export_builder_handoff.py", str(model), "--target", "lovable")
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("not-ready", result.stderr or result.stdout)

    def test_blocking_unknown_prevents_provisional_export(self) -> None:
        data = json.loads((FIXTURES / "valid-semantic-ia.json").read_text(encoding="utf-8"))
        data["unknowns"][0]["blocks_handoff"] = True
        with tempfile.TemporaryDirectory() as directory:
            model = Path(directory) / "blocked.json"
            model.write_text(json.dumps(data), encoding="utf-8")
            result = self.run_script("export_builder_handoff.py", str(model), "--target", "figma-make")
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("blocking unknown", result.stderr or result.stdout)

    def test_product_prototype_handoff_is_distinct_from_ia_blueprint(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            specification = Path(directory) / "prototype.md"
            launch = Path(directory) / "launch.txt"
            result = self.run_script(
                "export_builder_handoff.py",
                str(FIXTURES / "valid-semantic-ia.json"),
                "--target", "lovable",
                "--intent", "product-prototype",
                "-o", str(specification),
                "--launch-output", str(launch),
            )
            self.assertEqual(result.returncode, 0, result.stderr or result.stdout)
            prompt = specification.read_text(encoding="utf-8")
            launch_text = launch.read_text(encoding="utf-8")
            self.assertIn("Product Prototype from an Approved Information Architecture", prompt)
            self.assertIn("IA Reference Lock", prompt)
            self.assertIn("Do not present the internal IA diagram as the product interface", prompt)
            self.assertIn("product's information-architecture constraints", launch_text)

    def test_undirected_relationship_summary_uses_non_directional_symbol(self) -> None:
        data = json.loads((FIXTURES / "valid-semantic-ia.json").read_text(encoding="utf-8"))
        data["relationships"][0]["direction"] = "undirected"
        with tempfile.TemporaryDirectory() as directory:
            model = Path(directory) / "undirected.json"
            specification = Path(directory) / "handoff.md"
            model.write_text(json.dumps(data), encoding="utf-8")
            result = self.run_script("export_builder_handoff.py", str(model), "-o", str(specification))
            self.assertEqual(result.returncode, 0, result.stderr or result.stdout)
            prompt = specification.read_text(encoding="utf-8")
        self.assertIn("Project — Document", prompt)

    def test_release_and_package_metadata_are_consistent(self) -> None:
        version = (ROOT / "VERSION").read_text(encoding="utf-8").strip()
        skill = (ROOT / "SKILL.md").read_text(encoding="utf-8")
        readme = (ROOT / "README.md").read_text(encoding="utf-8")
        manifest = json.loads((PACKAGES / "manifest.json").read_text(encoding="utf-8"))
        self.assertRegex(version, r"^\d+\.\d+\.\d+$")
        self.assertIn(f'version: "{version}"', skill)
        self.assertIn(f"version-{version}-", readme)
        self.assertEqual(manifest["version"], version)
        self.assertEqual(manifest["packages"]["agent_skill"]["display_name"], "Agent Skill Package")
        self.assertEqual(manifest["packages"]["workspace_kit"]["display_name"], "Workspace Kit")

    def test_core_scope_preserves_ia_while_composing_requested_derivatives(self) -> None:
        skill = (ROOT / "SKILL.md").read_text(encoding="utf-8")
        self.assertRegex(skill, re.compile(r"sitemap.*page/destination", flags=re.IGNORECASE))
        self.assertRegex(skill, re.compile(r"user flow.*goal-directed action", flags=re.IGNORECASE))
        self.assertIn("minimum semantic substrate", skill)
        self.assertIn("IA Reference Lock", skill)
        self.assertIn("XML/SEO", skill)

    def test_decision_kernel_supports_novices_without_serial_questions(self) -> None:
        skill = (ROOT / "SKILL.md").read_text(encoding="utf-8")
        workspace = (PACKAGES / "workspace-kit" / "propaymun-ia-workspace-kit.md").read_text(encoding="utf-8")
        for content in (skill, workspace):
            self.assertIn("reversible", content.lower())
            self.assertIn("serial", content.lower())
            self.assertIn("ProPaymun", content)

    def test_high_priority_core_hides_internal_labels_and_adjacent_commitments(self) -> None:
        skill = (ROOT / "SKILL.md").read_text(encoding="utf-8")
        instructions = (PACKAGES / "workspace-kit" / "WORKSPACE_INSTRUCTIONS.md").read_text(encoding="utf-8")
        for content in (skill, instructions):
            lowered = content.lower()
            self.assertIn("ordinary conversation", lowered)
            self.assertIn("recommendation is not a", lowered)
            self.assertIn("registration", lowered)
            self.assertIn("growth", lowered)
        self.assertNotIn("recommend a clear Proposed starting point", instructions)

    def test_sitemap_contract_separates_destinations_from_neighboring_concepts(self) -> None:
        sitemap = (ROOT / "references" / "sitemap.md").read_text(encoding="utf-8")
        schema = json.loads((ROOT / "schema" / "product-sitemap.schema.json").read_text(encoding="utf-8"))
        self.assertIn("view or filter", sitemap)
        self.assertIn("capability", sitemap)
        self.assertIn("action/control", sitemap)
        destination = schema["properties"]["destinations"]["items"]
        self.assertIn("destination_kind", destination["required"])
        self.assertIn("views", schema["properties"])
        self.assertIn("states", schema["properties"])
        self.assertIn("capabilities", schema["properties"])

    def test_adaptive_stop_and_localization_are_in_both_packages(self) -> None:
        skill = (ROOT / "SKILL.md").read_text(encoding="utf-8")
        workspace = (PACKAGES / "workspace-kit" / "propaymun-ia-workspace-kit.md").read_text(encoding="utf-8")
        for content in (skill, workspace):
            lowered = content.lower()
            self.assertIn("adaptive sufficiency", lowered)
            self.assertIn("repeat this sufficiency check", lowered)
            self.assertIn("never infer a country", lowered)
            self.assertIn("short copy-ready launch instruction", content)

    def test_memory_isolation_and_token_discipline_are_in_both_packages(self) -> None:
        skill = (ROOT / "SKILL.md").read_text(encoding="utf-8")
        workspace = (PACKAGES / "workspace-kit" / "propaymun-ia-workspace-kit.md").read_text(encoding="utf-8")
        for content in (skill, workspace):
            self.assertIn("Current-turn authority and memory isolation", content)
            self.assertIn("Never create a file, presentation, diagram", content)
            self.assertIn("Do not proactively retrieve, search, read, create, or update persistent memory", content)
            self.assertIn("portable continuation note", content)
            self.assertIn("Project Knowledge", content)
            self.assertIn("Gem Knowledge", content)
            self.assertIn("Relevance and token discipline", content)
            self.assertIn("one representation at a time", content)

    def test_visual_builder_is_downstream_and_not_a_runtime(self) -> None:
        manifest = json.loads((PACKAGES / "manifest.json").read_text(encoding="utf-8"))
        skill = (ROOT / "SKILL.md").read_text(encoding="utf-8")
        self.assertIn("visual_builder_handoff", manifest)
        self.assertEqual(manifest["visual_builder_handoff"]["outputs"], ["markdown-specification", "short-launch-text"])
        self.assertIn("Do not use Figma Make", skill)
        self.assertFalse((ROOT / "adapters" / "figma-make").exists())

    def test_repository_uses_professional_package_names(self) -> None:
        readme = (ROOT / "README.md").read_text(encoding="utf-8")
        self.assertIn("Agent Skill Package", readme)
        self.assertIn("Workspace Kit", readme)
        self.assertIn("Machine-scannable install map", readme)
        self.assertNotIn("## Two supported distributions", readme)
        self.assertTrue((PACKAGES / "manifest.json").exists())
        self.assertFalse((ROOT / "adapters" / "manifest.json").exists())

    def test_installation_guidance_does_not_overclaim_hosts(self) -> None:
        for filename in ("README.md", "README.fa.md"):
            content = (ROOT / filename).read_text(encoding="utf-8")
            self.assertNotIn("Gemini CLI", content)
            self.assertNotIn("Kimi Projects", content)
            self.assertNotIn("Z.AI/GLM workspaces", content)
            self.assertIn("New Gem", content)
        self.assertIn("unverified", (ROOT / "README.md").read_text(encoding="utf-8").lower())
        self.assertIn("تأییدنشده", (ROOT / "README.fa.md").read_text(encoding="utf-8"))

    def test_capability_routing_does_not_require_diagram_companions(self) -> None:
        routing = (ROOT / "references" / "capability-routing.md").read_text(encoding="utf-8")
        self.assertIn("Route by capability, not brand", routing)
        self.assertIn("complete fallback", routing)
        self.assertIn("Do not require either companion", routing)

    def test_companion_activation_and_portable_contract_are_explicit(self) -> None:
        skill = (ROOT / "SKILL.md").read_text(encoding="utf-8")
        instructions = (PACKAGES / "workspace-kit" / "WORKSPACE_INSTRUCTIONS.md").read_text(encoding="utf-8")
        manifest = json.loads((PACKAGES / "manifest.json").read_text(encoding="utf-8"))
        for content in (skill, instructions):
            self.assertIn("product/UX sitemap", content)
            self.assertIn("user flow", content.lower())
            self.assertIn("minimum semantic substrate", content.lower())
        self.assertEqual(manifest["capabilities"]["companions"], ["product-sitemap", "user-flow"])
        self.assertEqual(manifest["companion_models"]["product_sitemap"], "schema/product-sitemap.schema.json")

    def test_behavioral_eval_has_critical_companion_and_memory_cases(self) -> None:
        cases = (ROOT / "evals" / "cases.yaml").read_text(encoding="utf-8")
        self.assertIn("version: 5", cases)
        self.assertIn("evaluation_contract:", cases)
        self.assertIn("journeys:", cases)
        for case_id in (
            "salon-coherent-provisional-pass",
            "explicit-persistent-memory-mutation",
            "standalone-product-sitemap",
            "xml-sitemap-ambiguity",
            "standalone-stateful-user-flow",
            "compound-ia-sitemap-flow",
            "workspace-kit-file-only-companions",
            "novice-status-language",
            "no-growth-commitment-drift",
            "sitemap-abstraction-separation",
            "rendered-flow-branch-legibility",
            "stage-complete-pause",
            "continue-later-without-persistence",
            "explicit-memory-continuation",
            "cross-project-memory-collision",
            "detailed-sitemap-destination-completeness",
            "preserve-explicit-product-direction",
            "social-commerce-from-idea-to-sitemap",
            "contaminated-memory-new-project",
            "pause-resume-portable-note",
            "explicit-memory-save-capability-split",
            "same-brief-cross-package-parity",
            "external-payment-stateful-flow",
        ):
            self.assertIn(f"id: {case_id}", cases)

    def test_eval_validator_requires_deep_journey_fields(self) -> None:
        validator = (ROOT / "scripts" / "validate_eval_cases.py").read_text(encoding="utf-8")
        requirements = (ROOT / "evals" / "requirements.txt").read_text(encoding="utf-8")
        for field in (
            "rubric_dimensions",
            "critical_failures",
            "unmeasured_layers",
            "multi_turn_journey_count",
            "package_routes",
        ):
            self.assertIn(field, validator)
        self.assertIn("PyYAML==", requirements)

    def test_eval_validator_rejects_shallow_or_malformed_catalogs_without_yaml_dependency(self) -> None:
        result = validate_data(
            {
                "version": 5,
                "skill": "propaymun-information-architecture",
                "evaluation_contract": {},
                "cases": [{"id": "duplicate"}],
                "journeys": [
                    {
                        "id": "duplicate",
                        "purpose": "Too shallow",
                        "priority": "critical",
                        "package_routes": ["agent-skill"],
                        "environment": {},
                        "turns": [{"user": "Test", "observe": {"must": [], "must_not": []}}],
                        "rubric_dimensions": [],
                        "critical_failures": [],
                        "unmeasured_layers": [],
                    }
                ],
            }
        )
        self.assertFalse(result["valid"])
        joined = "\n".join(result["errors"])
        self.assertIn("duplicate case or journey ids", joined)
        self.assertIn("at least three journeys", joined)
        self.assertIn("rubric_dimensions", joined)

    def test_phase_closure_and_portable_continuation_are_in_both_packages(self) -> None:
        skill = (ROOT / "SKILL.md").read_text(encoding="utf-8")
        workspace = (PACKAGES / "workspace-kit" / "propaymun-ia-workspace-kit.md").read_text(encoding="utf-8")
        discovery = (ROOT / "references" / "discovery.md").read_text(encoding="utf-8")
        for content in (skill, workspace):
            self.assertIn("stage-complete summary", content)
            self.assertIn("confirmed choices", content)
            self.assertIn("reversible assumptions", content)
            self.assertIn("optional continuations", content)
        self.assertIn("Phase closure and continuation", discovery)
        self.assertIn("project name or disambiguating identifier", discovery)

    def test_marketplace_modeling_and_sitemap_edge_cases_are_documented(self) -> None:
        modeling = (ROOT / "references" / "modeling.md").read_text(encoding="utf-8")
        sitemap = (ROOT / "references" / "sitemap.md").read_text(encoding="utf-8")
        self.assertIn("person or account distinct from the roles", modeling)
        self.assertIn("minimum trust and safety structure", modeling)
        self.assertIn("access gate is not the structural parent", sitemap)
        self.assertIn("cart is transient pre-purchase", sitemap)
        self.assertIn("must not replace the requested sitemap", sitemap)

    def test_release_gate_does_not_hide_critical_failures_in_aggregate(self) -> None:
        rubric = (ROOT / "evals" / "RUBRIC.md").read_text(encoding="utf-8")
        self.assertIn("cannot override a critical failure", rubric)
        self.assertNotIn("at least 85%", rubric)


if __name__ == "__main__":
    unittest.main()
