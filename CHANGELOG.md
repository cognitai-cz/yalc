# Changelog

## [0.3.0] - 2026-03-14

### Changed

- `ClientMetadataStrategy.handle` is now an `async` method.
- Metadata strategies are now executed concurrently via `asyncio.gather` instead of sequentially.

### Fixed

- Added `[build-system]` table to `pyproject.toml` so `uv` installs the package into the venv, resolving `ModuleNotFoundError: No module named 'yalc'` when running tests.

## [0.2.2] - 2026-03-10

### Fixed

- `LLMModel` enum initialisation now uses a provider model map instead of relying on enum value lookup, fixing a bug where model resolution could fail at import time.

## [0.2.1] - 2026-02-21

### Added

- Additional LLM models across Anthropic and OpenAI providers.
- `scripts/check_models.py` utility to verify model availability and pricing.
- Expanded README with usage examples.

## [0.2.0] - 2026-02-21

### Added

- Integration test suite covering `Client`, `AnthropicClient`, `OpenAIClient`, and `client_factory`.
- `CLAUDE.md` with development guidance for Claude Code.
- `TESTING.md` documenting the test architecture.
- `ClientMetadataStrategy` abstract base and support for multiple strategies per client.
- `anyio`, `pytest-mock`, and related dev dependencies.

## [0.1.0] - Initial release

### Added

- `Client` abstract base class with `structured_response` supporting optional context-based metadata dispatch.
- `AnthropicClient` and `OpenAIClient` provider implementations via `instructor`.
- `create_client` factory mapping `LLMModel` to the correct provider client.
- `LLMModel` `StrEnum` with `.provider`, `.provider_string`, and `.mode` properties.
- `PricingService` with TTL-cached per-token cost lookup from litellm.
- `ClientCall`, `ContextMessage`, and `ClientMessage` data types.
- `py.typed` marker for PEP 561 compliance.
- CI pipelines for linting and publishing.
