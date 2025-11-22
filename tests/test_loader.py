import pytest
from deepseek_v3_tokenizer.deepseek_tokenizer import load_text_files


@pytest.fixture
def temp_dir(tmp_path):
    """Fixture to create a temporary directory with some files."""
    d = tmp_path / "test_data"
    d.mkdir()
    (d / "file1.txt").write_text("content1", encoding="utf-8")
    (d / "file2.md").write_text("content2", encoding="utf-8")
    (d / "sub").mkdir()
    (d / "sub" / "file3.txt").write_text("content3", encoding="utf-8")
    return d


def test_load_text_files_default(temp_dir):
    """Test default behavior (txt only, non-recursive)."""
    result = load_text_files(str(temp_dir))
    assert "file1" in result
    assert result["file1"] == "content1"
    assert "file2" not in result
    assert "file3" not in result


def test_load_text_files_extensions(temp_dir):
    """Test with multiple extensions."""
    result = load_text_files(str(temp_dir), extensions=[".txt", ".md"])
    assert "file1" in result
    assert "file2" in result
    assert result["file2"] == "content2"


def test_load_text_files_recursive(temp_dir):
    """Test recursive search."""
    result = load_text_files(str(temp_dir), recursive=True)
    assert "file1" in result
    assert "file3" in result
    assert result["file3"] == "content3"


def test_load_text_files_empty_dir(tmp_path):
    """Test with empty directory."""
    empty_dir = tmp_path / "empty"
    empty_dir.mkdir()
    result = load_text_files(str(empty_dir))
    assert result == {}


def test_load_text_files_non_existent():
    """Test with non-existent directory."""
    result = load_text_files("non_existent_directory_12345")
    assert result == {}
