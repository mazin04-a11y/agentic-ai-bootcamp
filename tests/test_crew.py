"""
tests/test_crew.py — Unit tests for crew assembly and config loading.
Week 18 pattern: validate agent behaviour and config before deployment.
"""
import pytest
from pathlib import Path
import yaml
import sys

sys.path.insert(0, str(Path(__file__).parent.parent / "src"))


def test_agents_config_loads():
    config_path = Path(__file__).parent.parent / "config" / "agents.yaml"
    assert config_path.exists(), "agents.yaml must exist in config/"
    with open(config_path) as f:
        cfg = yaml.safe_load(f)
    assert "researcher" in cfg, "agents.yaml must define a 'researcher'"
    assert "writer" in cfg, "agents.yaml must define a 'writer'"
    for agent in ["researcher", "writer"]:
        assert "role" in cfg[agent]
        assert "goal" in cfg[agent]
        assert "backstory" in cfg[agent]


def test_tasks_config_loads():
    config_path = Path(__file__).parent.parent / "config" / "tasks.yaml"
    assert config_path.exists(), "tasks.yaml must exist in config/"
    with open(config_path) as f:
        cfg = yaml.safe_load(f)
    assert "research_task" in cfg
    assert "writing_task" in cfg
    for task in ["research_task", "writing_task"]:
        assert "description" in cfg[task]
        assert "expected_output" in cfg[task]


def test_task_description_accepts_topic():
    config_path = Path(__file__).parent.parent / "config" / "tasks.yaml"
    with open(config_path) as f:
        cfg = yaml.safe_load(f)
    topic = "test topic"
    formatted = cfg["research_task"]["description"].format(topic=topic)
    assert topic in formatted, "Task description must support {topic} placeholder"


def test_config_dir_structure():
    base = Path(__file__).parent.parent
    assert (base / "src" / "crew.py").exists()
    assert (base / "config" / "agents.yaml").exists()
    assert (base / "config" / "tasks.yaml").exists()
    assert (base / "requirements.txt").exists()
    assert (base / ".env.example").exists()
