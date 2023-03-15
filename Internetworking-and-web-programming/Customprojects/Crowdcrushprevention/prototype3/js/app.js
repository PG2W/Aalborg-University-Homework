import Grid from "./grid.js";
import Tools from "./tools.js";
import Agents from "./agents.js";

class App {
  constructor() {
    this.gridCanvas = document.getElementById("grid-canvas");
    this.toolCanvas = document.getElementById("tool-canvas");

    this.init();
  }

    init() {
      this.grid = new Grid(this.gridCanvas);
      this.tools = new Tools(this.toolCanvas, this.gridCanvas, this.grid); // Pass both canvases
      this.agents = new Agents(this.gridCanvas, this.grid);
    
      this.registerEventListeners();
      this.registerResizeEventListener();
    
      this.loop();
    }

    registerResizeEventListener() {
        window.addEventListener("resize", () => {
        this.grid.resize();
        });
    }

    registerEventListeners() {
    }

    loop() {
        this.agents.update();
        this.agents.draw();
        this.grid.draw();
        
        requestAnimationFrame(() => this.loop());
    }
    
}

const app = new App();
