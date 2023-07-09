compile:
	@mkdir -p src/compiled
	@protoc -I=. --python_out=./src/compiled ./regressor.proto
	@echo "Compilation done!"
