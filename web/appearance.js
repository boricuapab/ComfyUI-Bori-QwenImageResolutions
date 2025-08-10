import { app } from "../../scripts/app.js";

app.registerExtension({
    name: "Bori-QwenImageResolutions.appearance", // Extension name
    async nodeCreated(node) {
		console.log("Checking node:", node.comfyClass);
        // Check if the node's comfyClass starts with "Bori Qwen Image Resolution"
        if (node.comfyClass.startsWith("Bori Qwen Image Resolution")) {
            // Apply styling
            node.color = "#151800";
            node.bgcolor = "#199d98";
			console.log("Colorized:", node.comfyClass);
        }
    }
});