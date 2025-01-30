from cog import BasePredictor, Input, Path
import os
import subprocess

class Predictor(BasePredictor):
    def setup(self):
        """Load the model into memory to make running multiple predictions efficient"""
        # No specific setup needed for SVGDreamer as it's a script-based model
        pass

    def predict(self,
                style: str = Input(description="Style configuration for SVGDreamer", default="iconography"),
                prompt: str = Input(description="Text prompt for SVG generation", default="an image of Batman. full body action pose, complete detailed body, white background, high quality, 4K, ultra realistic"),
                token_ind: int = Input(description="Token index for the text prompt", default=1),
                result_path: str = Input(description="Path to save the result", default="./logs/output"),
                multirun: bool = Input(description="Run the script multiple times with different random seeds", default=False)
                ) -> Path:
        """Run a single prediction on the model"""
        # Create the result directory if it doesn't exist
        os.makedirs(result_path, exist_ok=True)

        # Prepare the command to run SVGDreamer
        command = [
            "python", "svgdreamer.py",
            f"x={style}",
            f"skip_sive=False",
            f"prompt='{prompt}'",
            f"token_ind={token_ind}",
            f"result_path={result_path}",
            f"multirun={multirun}"
        ]

        # Run the SVGDreamer script
        subprocess.run(command, check=True)

        # Return the path to the generated SVG file
        svg_file = os.path.join(result_path, "output.svg")
        return Path(svg_file)