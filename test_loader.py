from pathlib import Path
from deepseek_v3_tokenizer.deepseek_tokenizer import load_text_files


def test_load_text_files():
    # Setup test directory
    test_dir = Path("test_data")
    test_dir.mkdir(exist_ok=True)

    (test_dir / "file1.txt").write_text("content1")
    (test_dir / "file2.md").write_text("content2")
    (test_dir / "sub").mkdir(exist_ok=True)
    (test_dir / "sub" / "file3.txt").write_text("content3")

    try:
        # Test 1: Default behavior (txt only, non-recursive)
        print("Test 1: Default behavior")
        result = load_text_files(str(test_dir))
        assert "file1" in result
        assert result["file1"] == "content1"
        assert "file2" not in result
        assert "file3" not in result
        print("PASS")

        # Test 2: Multiple extensions
        print("Test 2: Multiple extensions")
        result = load_text_files(str(test_dir), extensions=[".txt", ".md"])
        assert "file1" in result
        assert "file2" in result
        assert result["file2"] == "content2"
        print("PASS")

        # Test 3: Recursive
        print("Test 3: Recursive")
        result = load_text_files(str(test_dir), recursive=True)
        assert "file1" in result
        assert "file3" in result
        assert result["file3"] == "content3"
        print("PASS")

    finally:
        # Cleanup
        import shutil

        if test_dir.exists():
            shutil.rmtree(test_dir)


if __name__ == "__main__":
    test_load_text_files()
