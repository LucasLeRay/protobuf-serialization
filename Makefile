compile:
	@mkdir src/compiled
	@protoc -I=. --python_out=./src/compiled ./person.proto
	@echo "Compilation done!"
