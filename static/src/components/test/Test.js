/* @odoo-module*/

import { Component, mount, whenReady, xml, useState } from "@odoo/owl";
import { templates } from "@web/core/assets";

export class Test extends Component {
    static template = "qweb_tutorial.Test";
    setup() {
        console.log("inside the setup method");
    }
}

whenReady(() => {
    const element = document.querySelector(".hello");
    console.log("element", element);
    if (element) {
        mount(Test, element, { templates });
    }
});
