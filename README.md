# robostudio-engine

`robostudio-engine` is the headless Python dataset engine and `robostudio` CLI
for inspecting, indexing, reviewing, clustering, probing, and exporting robotics
dataset metadata.

## At a Glance

| | |
| --- | --- |
| Job | Provide scriptable dataset operations for local review and CI without the desktop UI. |
| Built for | Robotics dataset engineers, review-tool builders, and automation owners. |
| Differentiator | One adapter contract across multiple dataset layouts plus local sidecar indexing and explicit export boundaries. |
| Produces | Episode inventories, SQLite indexes, thumbnails, QA reports, cluster manifests, probe reports, and metadata exports. |

## Install

Core commands have no required third-party runtime dependencies:

```bash
python -m pip install "robostudio-engine==0.1.1"
```

Install only the extras needed by a workflow:

```bash
python -m pip install "robostudio-engine[hdf5]==0.1.1"
python -m pip install "robostudio-engine[hf]==0.1.1"
python -m pip install "robostudio-engine[ml]==0.1.1"
python -m pip install "robostudio-engine[trust]==0.1.1"
```

The `ml` extra includes large model and clustering dependencies. The `trust`
extra installs the published companion trust tools used by the wrapper
commands.

## Verified Quickstart

Run from a source checkout:

```bash
robostudio inspect examples/mock_multi_format/lerobot_v3
```

The bundled fixture is detected as `lerobot` and reports two episodes. `inspect`
is read-only.

## Core Command Surface

| Commands | Evidence or side effect |
| --- | --- |
| `inspect` | JSON adapter name and normalized episode inventory. |
| `index`, `query` | SQLite index at `<dataset>/.robostudio/index.sqlite`. |
| `thumbs` | Thumbnail files under `<dataset>/.robostudio/thumbs/`. |
| `qa` | JSON or Markdown sensor QA findings. |
| `cluster` | Hash, CLIP, or custom-encoder failure clusters. |
| `export` | Local manifest, metadata bridge, Hugging Face preparation/upload, or intake ZIP. |
| `decode-info`, `plugins validate`, `smoke` | Local capability and contract checks. |

Adapters cover the checked-in LeRobot v2/v3, RLDS, OpenX, HDF5 profile,
rosbag, and folder-of-MP4-plus-JSONL shapes. Support is fixture-backed metadata
parsing, not a claim of compatibility with every producer or version.

## Companion Trust Tools

The engine contains executable wrappers for:

- `lerobot-quality-gates`;
- `robot-recovery-bench`;
- `vla-robustness-kit`;
- `embodiment-card`;
- `robotics-reviewkit`;
- `failure-gallery`.

These projects are not required by the core engine. Install the `trust` extra
before using `quality-gates`, `recovery`, `probe`, `card`, or failure-gallery
preview behavior. `robotics-reviewkit` remains a source-distributed companion
and must be installed separately for `validate-review`. In the AuraOne
monorepo, the engine can also discover sibling `src` directories.

## Runtime, Data, and Network Boundary

- Core adapters, indexing, QA, hash clustering, plugin validation, and local
  exports operate on local files.
- `index` and `thumbs` write inside the dataset's `.robostudio` directory.
  `ffmpeg` is invoked locally for supported thumbnail paths.
- `inspect`, metadata bridge exports, and some reports can contain local paths
  or source metadata. Review outputs before sharing.
- Training-ready manifest and intake exports scrub absolute paths and
  secret-like fields and exclude raw media. Metadata bridge JSONL preserves
  normalized episode metadata and needs separate review.
- Intake export writes a local ZIP with an intended destination; it does not
  transmit the packet.
- Hugging Face upload occurs only with the `hf` extra plus `HF_TOKEN` or
  `HUGGINGFACE_TOKEN`. Without them, the command prepares local files and a
  blocker note.
- CLIP clustering can download model files into `~/.cache/robostudio`; a custom
  encoder or BYO VLA policy runs an explicit local executable.

## Limitations

- Adapter support is fixture-backed parsing for known layouts, not a claim of
  compatibility with every dataset producer, codec, or schema revision.
- The wheel contains only `robostudio_engine`; companion trust tools are
  installed through the `trust` extra or discovered from a source checkout.
- `robotics-reviewkit` is not included in the `trust` extra because it is not a
  standalone PyPI distribution.

## Robotics Studio Open Integration

Robotics Studio Open documents that the `robostudio` CLI ships with its desktop
installers. That is a direct executable product integration. The standalone
package remains useful for CI and headless review without installing the
desktop application.

## Publication Status

Verified on 2026-07-13:

- PyPI: [`robostudio-engine==0.1.1`](https://pypi.org/project/robostudio-engine/0.1.1/)
- Source: [`auraoneai/robostudio-engine`](https://github.com/auraoneai/robostudio-engine)
- GitHub release: [`v0.1.1`](https://github.com/auraoneai/robostudio-engine/releases/tag/v0.1.1)
- The separate Robotics Studio Open product has a `v0.2.0` release; that product
  release is not a second `robostudio-engine` package release.
- Checked-in datasets and media are synthetic fixtures.

## Next Action

Run `inspect` against a copy of one review candidate, then run `qa` and inspect
all emitted paths and metadata before creating an export.
