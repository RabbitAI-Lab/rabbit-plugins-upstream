# Makefile for camsnap skill — local dev & release automation
# Usage: make <target>

SKILL_DIR := $(dir $(abspath $(lastword $(MAKEFILE_LIST))))
SCRIPTS   := $(SKILL_DIR)scripts
BUMP      ?= patch

.PHONY: help release publish quick dev dry-run autopublish version check clean

help: ## Show this help
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | \
		awk 'BEGIN {FS = ":.*?## "}; {printf "  \033[36m%-15s\033[0m %s\n", $$1, $$2}'

release: ## Full release: detect changes, bump version, sync docs, publish to ClawHub
	@$(SCRIPTS)/camsnap-release.sh --bump $(BUMP)

publish: release ## Alias for release

quick: ## Quick dev publish (auto dev version, skips changelog)
	@$(SCRIPTS)/camsnap-quick-publish.sh --bump $(BUMP)

dev: quick ## Alias for quick

dry-run: ## Preview release without publishing
	@$(SCRIPTS)/camsnap-release.sh --bump $(BUMP) --dry-run

autopublish: ## Auto-detect changes and publish if needed (for CI/hooks)
	@$(SCRIPTS)/camsnap-autopublish.sh --bump $(BUMP)

version: ## Show current version
	@echo "SKILL.md: $$(grep '^version:' $(SKILL_DIR)SKILL.md | head -1)"
	@echo "_meta.json: $$(grep '"version"' $(SKILL_DIR)_meta.json | head -1)"
	@if [ -f $(SKILL_DIR).clawhub/origin.json ]; then \
		echo "Published: $$(grep '"installedVersion"' $(SKILL_DIR).clawhub/origin.json)"; \
	fi

check: ## Validate skill structure and files
	@test -f $(SKILL_DIR)SKILL.md || (echo "MISSING: SKILL.md" && exit 1)
	@test -f $(SKILL_DIR)_meta.json || (echo "MISSING: _meta.json" && exit 1)
	@test -f $(SKILL_DIR)skill-card.md || (echo "MISSING: skill-card.md" && exit 1)
	@echo "✓ Skill structure OK"
	@# Check version sync
	@V1=$$(grep '^version:' $(SKILL_DIR)SKILL.md | sed 's/version: *//' | tr -d ' "'); \
	 V2=$$(grep '"version"' $(SKILL_DIR)_meta.json | head -1 | sed 's/.*"version": *"\([^"]*\)".*/\1/'); \
	 if [ "$$V1" = "$$V2" ]; then echo "✓ Version in sync: $$V1"; \
	 else echo "✗ Version mismatch: SKILL.md=$$V1 _meta.json=$$V2" && exit 1; fi

clean: ## Remove dev artifacts
	@rm -f $(SKILL_DIR)scripts/*.tmp
	@echo "✓ Cleaned"
