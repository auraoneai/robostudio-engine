from __future__ import annotations

from pathlib import Path

try:
    import tomllib
except ModuleNotFoundError:  # pragma: no cover
    import tomli as tomllib


ROOT = Path(__file__).resolve().parents[1]


def test_readme_discovery_sections():
    readme = (ROOT / "README.md").read_text(encoding="utf-8")
    for section in (
        "## At a Glance",
        "## Install",
        "## Verified Quickstart",
        "## Runtime, Data, and Network Boundary",
        "## Limitations",
        "## Publication Status",
        "## Next Action",
    ):
        assert section in readme


def test_pyproject_discovery_metadata():
    metadata = tomllib.loads((ROOT / "pyproject.toml").read_text(encoding="utf-8"))
    project = metadata["project"]
    assert project["readme"] == "README.md"
    assert project["authors"][0]["email"] == "opensource@auraone.ai"
    assert {"lerobot", "robotics", "rosbag", "vla"} <= set(project["keywords"])
    assert "Topic :: Scientific/Engineering :: Artificial Intelligence" in project["classifiers"]
    assert "Topic :: Scientific/Engineering :: Robotics" not in project["classifiers"]
    assert {"Source", "Documentation", "Issues", "Changelog", "Security", "Companion Tools"} <= set(project["urls"])
    assert {"hdf5", "hf", "ml", "trust"} <= set(project["optional-dependencies"])
    assert metadata["tool"]["setuptools"]["packages"]["find"]["include"] == ["robostudio_engine*"]
