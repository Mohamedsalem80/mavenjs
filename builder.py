import re

full = '''/*---------------------------------------*
 * Mohamed Salem Mohamed Soliman         *
 * mquery JavaScript Library             *
 * v1.0.2                                *
 * https://github.com/Mohamedsalem80     *
 *---------------------------------------*/

(function(global){

    if (!global.document) {
        throw new Error("maven error: a window with a document required");
    }

    function maven(selector, context){
        "use strict";
        return new start(selector, context);
    }

    maven.fn = maven.prototype = {
        version: "1.0.2",
        constructor: maven,
        ismaven: true,
        length: 0,
        add: function(obj){
            if(obj.ismaven){
                var t = 0;
                for(var i = this.length; t < obj.length; i++){
                    this[i] = obj[t];
                    t++;
                }
                this.selector += ", "+obj.selector;
                return this;
            } else {
                console.error("maven error: the passed object is not a maven");
            }
        },
        toArray: function(){
            return Array.from(this);
        },
        ready: function(func) {
            var _this = this;
            if (document.attachEvent ? document.readyState == "complete" : document.readyState != "loading") {
                func(this);
            } else {
                document.addEventListener('DOMContentLoaded',function(e){
                    func.call(e,_this,e);
                });
            }
            return this;
        },
        on: function (eventName,handler){
            var a = this.selector;
            document.addEventListener(eventName, function(e) {
                if ((e.target).matches(a)) {
                    handler.call(e.target,e);
                }  
            }, false);
        },
        off: function(event, callback) {
            for(var i=0; i < this.length; i++) {
                this[i].removeEventListener(event,callback);
            }
            return this;
        },
        css: function(prop, value) {
            props = [];
            if(value == null && typeof prop != "object"){
                for(var i=0; i < this.length; i++) {
                    var p = getComputedStyle(this[i])[prop];
                    props.push(p);
                }
                return props;
            } else {
                if(typeof prop == "object"){
                    for(var i=0; i < this.length; i++) {
                        for (const key in prop) {
                            this[i].style[key] = prop[key];
                        }
                    }
                } else{
                    for(var i=0; i < this.length; i++) {
                        this[i].style[prop] = value;
                    }
                }
                return this;
            }
        },
        scroll: function(callback) {
            window.addEventListener("scroll", function(e){callback.call(e,this)});
            return this;
        },
        scrollTo: function(x, y) {
            window.scroll(x, y);
            return this;
        },
        html: function(value) {
            if(value == null) {
                var e = [];
                for(var i=0; i < this.length; i++) {
                    e.push(this[i].outerHTML);
                }
                return e;
            } else {
                for(var i=0; i < this.length; i++) {
                    this[i].outerHTML = value;
                }
            }
        },
        text: function(value) {
            if(value == null) {
                var e = [];
                for(var i=0; i < this.length; i++) {
                    e.push(this[i].textContent);
                }
                return e;
            } else {
                for(var i=0; i < this.length; i++) {
                    this[i].innerHTML = value;
                }
                return this;
            }
        },
        trigger: function(event) {
            for(var i=0; i < this.length; i++) {
                this[i][event]();
            }
            return this;
        },
        each: function(callback) {
            for(var i=0; i < this.length; i++) {
                callback(this[i], i);
            }
        },
        map: function(callback) {
            var e = [];
            for(var i=0; i < this.length; i++) {
                var a = callback(this[i], i);
                if(a != null){
                    e.push(a);
                }
            }
            return e;
        },
        slice: function(begin, end){
            return maven(this.toArray().slice(begin, end));
        },
        find: function(query){
            var e = [];
            for(var i=0; i < this.length; i++) {
                if(maven.selectar(query,this[i]).length){
                    e.push(maven.selectar(query,this[i]));
                }
            }
            return maven(maven.unique(maven.flatten(e)));
        },
        filter: function(query){
            var e = [];
            for(var i=0; i < this.length; i++) {
                if(this[i].matches(query)){
                    e.push(this[i]);
                }
            }
            return maven(e);
        },
        is: function(query){
            for(var i=0; i < this.length; i++) {
                if(this[i].matches(query)){
                    return true;
                }
            }
        },
        not: function(query){
            var e = [];
            for(var i=0; i < this.length; i++) {
                if(!this[i].matches(query)){
                    e.push(this[i]);
                }
            }
            return maven(e);
        },
        contains: function(text){
            var e = [];
            for(var i=0; i < this.length; i++) {
                if(this[i].innerHTML.includes(text)){
                    e.push(this[i]);
                }
            }
            return maven(e);
        },
        has: function(query){
            var e = [];
            for(var i=0; i < this.length; i++) {
                var a = Array.from(this[i].children);
                for(var t = 0; t < a.length; t++){
                    if(a[t].matches(query)){
                        e.push(this[i]);
                    }
                }
            }
            return maven(maven.unique(e));
        },
        children: function() {
            var e = [];
            for(var i=0; i < this.length; i++) {
                e.push(Array.from(this[i].children));
            }
            return maven(maven.unique(maven.flatten(e)));
        },
        parents: function() {
            var e = [];
            for(var i=0; i < this.length; i++) {
                var a = this[i];
                var p = [];
                while (a) {
                    p.push(a);
                    a = a.parentNode;
                }
                p.shift().pop();
                p = Array.from(p);
                e.push(p);
            }
            return maven(maven.unique(maven.flatten(e)));
        },
        siblings: function() {
        var e = [];
        for(var i=0; i < this.length; i++) {
        e.push(Array.from(this[i].parentNode.children));
        e[i] = e[i].filter(w => w != this[i]);
        }
        return maven(maven.unique(maven.flatten(e)));
        },
        nextAll: function() {
            var e = [];
            for(var i=0; i < this.length; i++) {
                var a = this[i];
                while(a.nextElementSibling){
                    e.push(a.nextElementSibling);
                    a = a.nextElementSibling;
                }
            }
            return maven(maven.unique(maven.flatten(e)));
        },
        prevAll: function() {
            var e = [];
            for(var i=0; i < this.length; i++) {
                var a = this[i];
                while(a.previousElementSibling){
                    e.push(a.previousElementSibling);
                    a = a.previousElementSibling;
                }
            }
            return maven(maven.unique(maven.flatten(e)));
        },
        show: function() {
            for(var i=0; i < this.length; i++) {
                this[i].style.display='';
            }
            return this;
        },
        hide: function() {
            for(var i=0; i < this.length; i++) {
                this[i].style.display='none';
            }
            return this;
        },
        empty: function() {
            for(var i=0; i < this.length; i++) {
                this[i].innerHTML = "";
            }
            return this;
        },
        remove: function() {
            for(var i=0; i < this.length; i++) {
                this[i].remove();
            }
            return this;
        },
        append: function(content) {
            for(var i=0; i < this.length; i++) {
                this[i].insertAdjacentHTML('beforeend', content);
            }
            return this;
        },
        prepend: function(content) {
            for(var i=0; i < this.length; i++) {
                this[i].insertAdjacentHTML('afterbegin', content);
            }
            return this;
        },
        after: function(content) {
            for(var i=0; i < this.length; i++) {
                this[i].insertAdjacentHTML("afterend", content);
            }
            return this;
        },
        before: function(content) {
            for(var i=0; i < this.length; i++) {
                this[i].insertAdjacentHTML("beforebegin", content);
            }
            return this;
        },
        addClass: function(Class) {
            for(var i=0; i < this.length; i++) {
                this[i].classList.add(Class);
            }
            return this;
        },
        removeClass: function(Class) {
            for(var i=0; i < this.length; i++) {
                this[i].classList.remove(Class);
            }
            return this;
        },
        classToggle: function(Class) {
            for(var i=0; i < this.length; i++) {
                this[i].classList.toggle(Class);
            }
            return this;
        },
        hasClass: function(Class, a) {
            if(a){
                var e = [];
                for(var i=0; i < this.length; i++) {
                    e.push(this[i].classList.contains(Class));
                }
                return e;
            } else {
                return this[i].classList.contains(Class);
            }
        },
        fadeToggle: function(duration) {
            if (duration == null) duration = 1000;
            for(var i = 0; i < this.length; i++) {
                var ele = this[i];
                var dis = getComputedStyle(ele).display;
                new fadeToggle_(ele, dis, duration);
            }
        },
        slideToggle: function(duration) {
            if (duration == null) duration = 1000;
            for(var i=0; i < this.length; i++) {
                var ele = this[i];
                var dis = getComputedStyle(ele).display;
                new slideToggle_(ele, dis, duration);
            }
        },
        val: function(vale) {
            if (vale == null) {
                var e = [];
                for(var i=0; i < this.length; i++) {
                    e.push(this[i].value);
                }
                return e;
            } else {
                for(var i=0; i < this.length; i++) {
                    this[i].value = vale;
                }
                return this;
            }
        },
        len: function() {
            var e = [];
            for(var i=0; i < this.length; i++) {
            e.push(this[i].value.length);
            }
            return e;
        },
        submit: function() {
            for(var i=0; i < this.length; i++) {
                this[i].submit();
            }
            return this;
        },
        serialize: function(){
            var kvpairs = [];
            for (var i = 0; i < this.length; i++) {
                var form = this[i]
                for ( var i = 0; i < form.elements.length; i++ ) {
                    var e = form.elements[i];
                    if(e.type){
                        if (e.type == "reset" || e.type == "submit" || e.tagName == "BUTTON") 	continue;
                        kvpairs.push(encodeURIComponent(e.name) + "=" + encodeURIComponent(e.value));
                    }
                }
            }
            return kvpairs.join("&");
        },
        removeProp: function(name) {
            for(var i=0; i < this.length; i++) {
                delete this[i][name];
            }
            return this;
        },
        prop: function(name, value){
            if(value == null && typeof name != "object"){
                var e = [];
                for(var i=0; i < this.length; i++) {
                    e.push(this[i][name]);
                }
                return e;
            } else if (typeof name == "object"){
                for(var i=0; i < this.length; i++) {
                    for (const key in name) {
                        this[i][key] = name[key];
                    }
                }
            } else {
                for(var i=0; i < this.length; i++) {
                    this[i][name] = value;
                }
            }
            return this;
        },
        removeAttr: function(name){
            for(var i=0; i < this.length; i++) {
                this[i].removeAttribute(name);
            }
            return this;
        },
        attr: function(name, value) {
            if(value == null && typeof name != "object"){
                var e = [];
                for(var i=0; i < this.length; i++) {
                    e.push(this[i].getAttribute(name));
                }
                return e;
            } else if (typeof name == "object"){
                for(var i=0; i < this.length; i++) {
                    for (const key in name) {
                        this[i].setAttribute(key, name[key]);
                    }
                }
                return this;
            } else {
                for(var i=0; i < this.length; i++) {
                    this[i].setAttribute(name, value);
                }
                return this;
            }
        },
        data: function(key,value){
            if(key == null && value == null){
                var mvnd = [];
                for(var i=0; i < this.length; i++) {
                    if(!this[i].getAttribute("mvn-data")){
                        mvnd.push(null);
                    } else {
                        mvnd.push(this[i].getAttribute("mvn-data"));
                    }
                }
                return mvnd;
            } else {
                var owned = [key,value];
                for(var i=0; i < this.length; i++) {
                    if(!this[i].getAttribute("mvn-data")){
                        this[i].setAttribute("mvn-data","[]");
                    }
                    var saved = JSON.parse(this[i].getAttribute("mvn-data"));
                    saved.push(owned);
                    var t = JSON.stringify(saved);
                    this[i].setAttribute("mvn-data", t)
                }
            }
            return this;
        },
        addSelf: function(){
            if(!this.prevObject){
                console.error("maven error: there is no previous object to add");
            } else {
                var t = 0;
                for(var i = this.length; t < this.prevObject.length; i++){
                    this[i] = this.prevObject[t];
                    t++;
                }
            }
            return this;
        },
    }

    var flatten = maven.flatten = function(arr){
        var temp = [];
        function loop(atr){
            for (var i = 0; i < atr.length; i++) {
                if(Array.isArray(atr[i])){
                    loop(atr[i]);
                } else {
                    temp.push(atr[i]);
                }
            }
        }
        loop(arr);
        return temp;
    }

    var xss = maven.xss = function(str) {
        const lt = /</g;//60
        const gt = />/g;//61
        const ap = /'/g;//39
        const ic = /"/g;//34
        const st = /!/g;//33
        const sl = /\//g;//47
        const ds = /-/g;//8208
        return str.toString()
                  .replace(st, "&#33;")
                  .replace(ic, "&#34;")
                  .replace(ap, "&#39;")
                  .replace(sl, "&#47;")
                  .replace(lt, "&#60;")
                  .replace(gt, "&#61;")
                  .replace(ds, "&#8208;");
    }

    var ajax = maven.ajax = function(url, method, data, callback, header="application/x-www-form-urlencoded; charset=UTF-8") {
        const request = new XMLHttpRequest();
        request.open(method, url, true);
        request.setRequestHeader("Content-Type", header);
        request.onload = () => {
            if (request.status >= 200 && request.status < 400) {
                const d = request.responseText;
                callback(d, request);
            } else {
                var tof;
                try {
                    var ad = request.status+" "+_ajrescd_[request.status];
                    tof = true;
                } catch(e) {
                    tof = false;
                }
                let errcod = tof ? ad : request.status;
                console.error("mquery error: The ajax request returned an error: #"+errcod);
            }
        };
        request.onerror = (message, source, lineno, colno, error) => {
            console.error("mquery error: The ajax request returned an error: "+message);
        };
        request.send(data);
    }

    var Import = maven.import = function(source, callback) {
        let script = document.createElement("script");
        const prior = document.getElementsByTagName("script")[0];
        script.async = 1;

        script.onload = script.onreadystatechange = (_, isAbort) => {
            if (isAbort || !script.readyState || /loaded|complete/.test(script.readyState)) {
                script.onload = script.onreadystatechange = null;
                script = undefined;

                if (!isAbort) {
                    if (callback) callback();
                }
            }
        };

        script.src = source;
        prior.parentNode.insertBefore(script, prior);
    }

    var parseHTML = maven.parseHTML = function(str) {
        var tmp = document.implementation.createHTMLDocument();
        tmp.body.innerHTML = str;
        return tmp.body.children;
    };

    var copy = maven.copy = function(text) {
        let target = document.createElement("textarea");
        target.style.position = "absolute";
        target.style.left = "-9999px";
        target.style.top = "0";
        target.textContent = text;
        document.body.appendChild(target);
        target.select();
        target.setSelectionRange(0, target.value.length);

        try {
            document.execCommand("copy");
            target.remove();
        } catch (e) {
            window.prompt("Copy to clipboard: Ctrl+C, Enter", text);
        }
    }

    var unique = maven.unique = function(arr){
        return [...new Set(arr)];
    }

    maven.id = "maven" + ( maven.fn.version + Math.random() ).replace(/\D/g,"");

    var selectar = maven.find = function(selector,context){
        context = context || document;
        var fx = {
            eq: function(i,f){
                return selectar(f,context)[i];
            },
            gt: function(n,f){
                var fmd = selectar(f,context);
                var als = [];
                n = isNaN(Number(n))?0:Number(n);
                var i = (Number(n)+1);
                while(i > n && i < fmd.length){
                    als.push(fmd[i]);
                    i++;
                }
                return als;
            },
            lt: function(n,f){
                var fmd = selectar(f,context);
                var als = [];
                n = isNaN(Number(n))?fmd.length:Number(n);
                var i = n-1;
                while(i < n && i >= 0){
                    als.push(fmd[i]);
                    i--;
                }
                return als;
            },
        },
        booleans = /(.+)(?:\:)(checked|selected|async|autofocus|autoplay|controls|defer|disabled|hidden|ismap|loop|multiple|open|readonly|required)/g,
        contexts = /(.+)(?:\:)(eq|gt|lt)\(([+|-]?\d)\)/g,
        tags = /[<](\w+)[>]/g;

        var rtd = selector;
        var elements = [];
        var types = selector.trim().split(",");
        for (var i = 0; i < types.length; i++) {
            types[i].trim()
            if(booleans.test(types[i])){
                types[i].replace(booleans,function(m,s1,s2){
                    try {
                        elements.push([...context.querySelectorAll(m)]);
                    } catch (e){
                        var els = [];
                        var als = selectar(s1,context);
                        for (var i = 0; i < als.length; i++) {
                            if(als[i][s2]) els.push(als[i]);
                        }
                    }
                });
            } else if(contexts.test(types[i])){
                types[i].replace(contexts, function(m,s1,s2,s3){
                    try {
                        elements.push([...context.querySelectorAll(m)]);
                    } catch (e){
                        if(fx[s2](s3,s1)) elements.push(fx[s2](s3,s1));
                    };
                });
            } else if(tags.test(types[i])){
                types[i].replace(tags,function(m,s1){
                    try {
                        elements.push([...context.querySelectorAll(m)]);
                    } catch (e){
                        elements.push(selectar(s1,context));
                    }
                });
            } else {
                try {
                    elements.push([...context.querySelectorAll(types[i])]);
                } catch (e){
                    console.error("maven error: out of range selector")
                }
            }
        }
        return maven.flatten([... new Set(elements)]);
    }

    start = maven.fn.start = function(selector, context){
        if(maven.next){
            this.prevObject = maven.next;
        }

        if (!selector) {
            return this;
        }
        else if(!context){
            context = document;
        }
        else if(context.ismaven){
            context = context[0];
        }
        else if(typeof context == "string"){
            context = document.querySelector(context);
        } 
        else if(context.tagName || context.nodeType){
            context = context;
        }
        else {
            context = document;
        }

        if(typeof selector == "string"){
            var elements = maven.find(selector,context);
            this.length = elements.length;
            for(var i = 0; i < elements.length; i++){
                this[i] = elements[i];
            }
        } else if(typeof selector == "function"){
            var _this = this;
            if (document.attachEvent ? document.readyState == "complete" : document.readyState != "loading") {
                selector(this);
            } else {
                document.addEventListener('DOMContentLoaded',function(e){
                    selector.call(e,_this,e)
                });
            }
        } else if(selector.ismaven){
            this.length = selector.length;
            for(var i = 0; i < selector.length; i++){
                this[i] = selector[i];
            }
        } else if(Array.isArray(selector)){
            var elements = selector;
            for(var i = 0; i < elements.length; i++){
                this[i] = elements[i];
            }
            this.length = elements.length;
        } else if(selector.tagName || selector.nodeType){
            this[0] = selector;
            this.length = 1;
        } else if(selector == document ||selector == window){
            this[0] = selector;
            this.length = 1;
        } else if(selector instanceof NodeList){
            var elements = [...selector];
            for(var i = 0; i < elements.length; i++){
                this[i] = elements[i];
            }
            this.length = elements.length;
        } else if(selector instanceof Object){
            this[0] = selector;
            this.length = 1;
        }
    
        this.selector = selector;
        maven.next = this;
        return this;
    }

    start.prototype = maven.fn;

    function fadeToggle_(ele, dis, duration){
        this.ele = ele;
        this.dis = dis;
        this.duration = duration;
        if (dis == "none") {
            this.ele.style.opacity = "0";
            this.ele.style.display = "block";
            this.ele.style.transition = "all "+this.duration+"ms";
            setTimeout(function() {
                ele.style.opacity="1";
            }, 15);
        } else {
            this.ele.style.opacity = "1";
            this.ele.style.transition="all "+this.duration+"ms";
            setTimeout(function() {
                ele.style.opacity="0";
            }, 10);
            setTimeout(function(){
                ele.style.display="none";
            }, duration+10);
        }
    }

    function slideToggle_(ele, dis, duration) {
        this.ele = ele;
        this.dis = dis;
        this.duration = duration;
        if (dis == "none") {
            this.ele.style.display = "block";
            this.ele.style.maxHeight = "0";
            var h = this.ele.scrollHeight + "px";
            this.ele.style.transition = "all "+this.duration+"ms";
            setTimeout(function() {
                ele.style.maxHeight = h;
            }, 10);
        } else {
            var h = this.ele.scrollHeight+"px";
            this.ele.style.maxHeight = h;
            this.ele.style.overflow = "hidden";
            this.ele.style.transition="all "+this.duration+"ms";
            setTimeout(function(){
                ele.style.maxHeight="0";
            }, 10);
            setTimeout(function() {
                ele.style.display="none";
            }, this.duration+1);
        }
    }

    var noConflict = maven.noConflict = function(deep) {
        if ( window.mvn === maven ) {
            window.mvn = _mvn;
        }
        if (deep && window.maven === maven) {
            window.maven = _maven;
        }
        return maven;
    }
    maven.noConflict(this);

    window.maven = window.mvn = maven;

})(this);'''

mvn_file_start = '''/*---------------------------------------*
 * Mohamed Salem Mohamed Soliman         *
 * mquery JavaScript Library             *
 * v1.0.2                                *
 * https://github.com/Mohamedsalem80     *
 *---------------------------------------*/

(function(global){

    if (!global.document) {
        throw new Error("maven error: a window with a document required");
    }

    function maven(selector, context){
        "use strict";
        return new start(selector, context);
    }
'''

mvn_proto_start = '''
    maven.fn = maven.prototype = {
        version: "1.0.2",
        constructor: maven,
        ismaven: true,
        length: 0,
'''

mvn_funcs = {
    "add" : '''
        add: function(obj){
            if(obj.ismaven){
                var t = 0;
                for(var i = this.length; t < obj.length; i++){
                    this[i] = obj[t];
                    t++;
                }
                this.selector += ", "+obj.selector;
                return this;
            } else {
                console.error("maven error: the passed object is not a maven");
            }
        },
''',

"toArray" : '''
        toArray: function(){
            return Array.from(this);
        },
''',

"ready" : '''
        ready: function(func) {
            var _this = this;
            if (document.attachEvent ? document.readyState == "complete" : document.readyState != "loading") {
                func(this);
            } else {
                document.addEventListener('DOMContentLoaded',function(e){
                    func.call(e,_this,e);
                });
            }
            return this;
        },
''',

"on" : '''
        on: function (eventName,handler){
            var a = this.selector;
            document.addEventListener(eventName, function(e) {
                if ((e.target).matches(a)) {
                    handler.call(e.target,e);
                }
            }, false);
        },
''',

"off" : '''
        off: function(event, callback) {
            for(var i=0; i < this.length; i++) {
                this[i].removeEventListener(event,callback);
            }
            return this;
        },
''',

"css" : '''
        css: function(prop, value) {
            props = [];
            if(value == null && typeof prop != "object"){
                for(var i=0; i < this.length; i++) {
                    var p = getComputedStyle(this[i])[prop];
                    props.push(p);
                }
                return props;
            } else {
                if(typeof prop == "object"){
                    for(var i=0; i < this.length; i++) {
                        for (const key in prop) {
                            this[i].style[key] = prop[key];
                        }
                    }
                } else{
                    for(var i=0; i < this.length; i++) {
                        this[i].style[prop] = value;
                    }
                }
                return this;
            }
        },
''',

"scroll" : '''
        scroll: function(callback) {
            window.addEventListener("scroll", function(e){callback.call(e,this)});
            return this;
        },
''',

"scrollTo" : '''
        scrollTo: function(x, y) {
            window.scroll(x, y);
            return this;
        },
''',

"html" : '''
        html: function(value) {
            if(value == null) {
                var e = [];
                for(var i=0; i < this.length; i++) {
                    e.push(this[i].outerHTML);
                }
                return e;
            } else {
                for(var i=0; i < this.length; i++) {
                    this[i].outerHTML = value;
                }
            }
        },
''',

"text" : '''
        text: function(value) {
            if(value == null) {
                var e = [];
                for(var i=0; i < this.length; i++) {
                    e.push(this[i].textContent);
                }
                return e;
            } else {
                for(var i=0; i < this.length; i++) {
                    this[i].innerHTML = value;
                }
                return this;
            }
        },
''',

"trigger" : '''
        trigger: function(event) {
            for(var i=0; i < this.length; i++) {
                this[i][event]();
            }
            return this;
        },
''',

"each" : '''
        each: function(callback) {
            for(var i=0; i < this.length; i++) {
                callback(this[i], i);
            }
        },
''',

"map" : '''
        map: function(callback) {
            var e = [];
            for(var i=0; i < this.length; i++) {
                var a = callback(this[i], i);
                if(a != null){
                    e.push(a);
                }
            }
            return e;
        },
''',

"slice" : '''
        slice: function(begin, end){
            return maven(this.toArray().slice(begin, end));
        },
''',

"find" : '''
        find: function(query){
            var e = [];
            for(var i=0; i < this.length; i++) {
                if(maven.selectar(query,this[i]).length){
                    e.push(maven.selectar(query,this[i]));
                }
            }
            return maven(maven.unique(maven.flatten(e)));
        },
''',

"filter" : '''
        filter: function(query){
            var e = [];
            for(var i=0; i < this.length; i++) {
                if(this[i].matches(query)){
                    e.push(this[i]);
                }
            }
            return maven(e);
        },
''',

"is" : '''
        is: function(query){
            for(var i=0; i < this.length; i++) {
                if(this[i].matches(query)){
                    return true;
                }
            }
        },
''',

"not" : '''
        not: function(query){
            var e = [];
            for(var i=0; i < this.length; i++) {
                if(!this[i].matches(query)){
                    e.push(this[i]);
                }
            }
            return maven(e);
        },
''',

"contains" : '''
        contains: function(text){
            var e = [];
            for(var i=0; i < this.length; i++) {
                if(this[i].innerHTML.includes(text)){
                    e.push(this[i]);
                }
            }
            return maven(e);
        },
''',

"has" : '''
        has: function(query){
            var e = [];
            for(var i=0; i < this.length; i++) {
                var a = Array.from(this[i].children);
                for(var t = 0; t < a.length; t++){
                    if(a[t].matches(query)){
                        e.push(this[i]);
                    }
                }
            }
            return maven(maven.unique(e));
        },
''',

"children" : '''
        children: function() {
            var e = [];
            for(var i=0; i < this.length; i++) {
                e.push(Array.from(this[i].children));
            }
            return maven(maven.unique(maven.flatten(e)));
        },
''',

"parents" : '''
        parents: function() {
            var e = [];
            for(var i=0; i < this.length; i++) {
                var a = this[i];
                var p = [];
                while (a) {
                    p.push(a);
                    a = a.parentNode;
                }
                p.shift().pop();
                p = Array.from(p);
                e.push(p);
            }
            return maven(maven.unique(maven.flatten(e)));
        },
''',

"siblings" : '''
        siblings: function() {
            var e = [];
            for(var i=0; i < this.length; i++) {
                e.push(Array.from(this[i].parentNode.children));
                e[i] = e[i].filter(w => w != this[i]);
            }
            return maven(maven.unique(maven.flatten(e)));
        },
''',

"nextAll" : '''
        nextAll: function() {
            var e = [];
            for(var i=0; i < this.length; i++) {
                var a = this[i];
                while(a.nextElementSibling){
                    e.push(a.nextElementSibling);
                    a = a.nextElementSibling;
                }
            }
            return maven(maven.unique(maven.flatten(e)));
        },
''',

"prevAll" : '''
        prevAll: function() {
            var e = [];
            for(var i=0; i < this.length; i++) {
                var a = this[i];
                while(a.previousElementSibling){
                    e.push(a.previousElementSibling);
                    a = a.previousElementSibling;
                }
            }
            return maven(maven.unique(maven.flatten(e)));
        },
''',

"show" : '''
        show: function() {
            for(var i=0; i < this.length; i++) {
                this[i].style.display='';
            }
            return this;
        },
''',

"hide" : '''
        hide: function() {
            for(var i=0; i < this.length; i++) {
                this[i].style.display='none';
            }
            return this;
        },
''',

"empty" : '''
        empty: function() {
            for(var i=0; i < this.length; i++) {
                this[i].innerHTML = "";
            }
            return this;
        },
''',

"remove" : '''
        remove: function() {
            for(var i=0; i < this.length; i++) {
                this[i].remove();
            }
            return this;
        },
''',

"append" : '''
        append: function(content) {
            for(var i=0; i < this.length; i++) {
                this[i].insertAdjacentHTML('beforeend', content);
            }
            return this;
        },
''',

"prepend" : '''
        prepend: function(content) {
            for(var i=0; i < this.length; i++) {
                this[i].insertAdjacentHTML('afterbegin', content);
            }
            return this;
        },
''',

"after" : '''
        after: function(content) {
            for(var i=0; i < this.length; i++) {
                this[i].insertAdjacentHTML("afterend", content);
            }
            return this;
        },
''',

"before" : '''
        before: function(content) {
            for(var i=0; i < this.length; i++) {
                this[i].insertAdjacentHTML("beforebegin", content);
            }
            return this;
        },
''',

"addClass" : '''
        addClass: function(Class) {
            for(var i=0; i < this.length; i++) {
                this[i].classList.add(Class);
            }
            return this;
        },
''',

"removeClass" : '''
        removeClass: function(Class) {
            for(var i=0; i < this.length; i++) {
                this[i].classList.remove(Class);
            }
            return this;
        },
''',

"classToggle" : '''
        classToggle: function(Class) {
            for(var i=0; i < this.length; i++) {
                this[i].classList.toggle(Class);
            }
            return this;
        },
''',

"hasClass" : '''
        hasClass: function(Class, a) {
            if(a){
                var e = [];
                for(var i=0; i < this.length; i++) {
                    e.push(this[i].classList.contains(Class));
                }
                return e;
            } else {
                return this[i].classList.contains(Class);
            }
        },
''',

"fadeToggle" : '''
        fadeToggle: function(duration) {
            if (duration == null) duration = 1000;
            for(var i = 0; i < this.length; i++) {
                var ele = this[i];
                var dis = getComputedStyle(ele).display;
                new fadeToggle_(ele, dis, duration);
            }
        },
''',

"slideToggle" : '''
        slideToggle: function(duration) {
            if (duration == null) duration = 1000;
            for(var i=0; i < this.length; i++) {
                var ele = this[i];
                var dis = getComputedStyle(ele).display;
                new slideToggle_(ele, dis, duration);
            }
        },
''',

"val" : '''
        val: function(vale) {
            if (vale == null) {
                var e = [];
                for(var i=0; i < this.length; i++) {
                    e.push(this[i].value);
                }
                return e;
            } else {
                for(var i=0; i < this.length; i++) {
                    this[i].value = vale;
                }
                return this;
            }
        },
''',

"len" : '''
        len: function() {
            var e = [];
            for(var i=0; i < this.length; i++) {
            e.push(this[i].value.length);
            }
            return e;
        },
''',

"submit" : '''
        submit: function() {
            for(var i=0; i < this.length; i++) {
                this[i].submit();
            }
            return this;
        },
''',

"serialize" : '''
        serialize: function(){
            var kvpairs = [];
            for (var i = 0; i < this.length; i++) {
                var form = this[i]
                for ( var i = 0; i < form.elements.length; i++ ) {
                    var e = form.elements[i];
                    if(e.type){
                        if (e.type == "reset" || e.type == "submit" || e.tagName == "BUTTON")   continue;
                        kvpairs.push(encodeURIComponent(e.name) + "=" + encodeURIComponent(e.value));
                    }
                }
            }
            return kvpairs.join("&");
        },
''',

"removeProp" : '''
        removeProp: function(name) {
            for(var i=0; i < this.length; i++) {
                delete this[i][name];
            }
            return this;
        },
''',

"prop" : '''
        prop: function(name, value){
            if(value == null && typeof name != "object"){
                var e = [];
                for(var i=0; i < this.length; i++) {
                    e.push(this[i][name]);
                }
                return e;
            } else if (typeof name == "object"){
                for(var i=0; i < this.length; i++) {
                    for (const key in name) {
                        this[i][key] = name[key];
                    }
                }
            } else {
                for(var i=0; i < this.length; i++) {
                    this[i][name] = value;
                }
            }
            return this;
        },
''',

"removeAttr" : '''
        removeAttr: function(name){
            for(var i=0; i < this.length; i++) {
                this[i].removeAttribute(name);
            }
            return this;
        },
''',

"attr" : '''
        attr: function(name, value) {
            if(value == null && typeof name != "object"){
                var e = [];
                for(var i=0; i < this.length; i++) {
                    e.push(this[i].getAttribute(name));
                }
                return e;
            } else if (typeof name == "object"){
                for(var i=0; i < this.length; i++) {
                    for (const key in name) {
                        this[i].setAttribute(key, name[key]);
                    }
                }
                return this;
            } else {
                for(var i=0; i < this.length; i++) {
                    this[i].setAttribute(name, value);
                }
                return this;
            }
        },
''',

"data" : '''
        data: function(key,value){
            if(key == null && value == null){
                var mvnd = [];
                for(var i=0; i < this.length; i++) {
                    if(!this[i].getAttribute("mvn-data")){
                        mvnd.push(null);
                    } else {
                        mvnd.push(this[i].getAttribute("mvn-data"));
                    }
                }
                return mvnd;
            } else {
                var owned = [key,value];
                for(var i=0; i < this.length; i++) {
                    if(!this[i].getAttribute("mvn-data")){
                        this[i].setAttribute("mvn-data","[]");
                    }
                    var saved = JSON.parse(this[i].getAttribute("mvn-data"));
                    saved.push(owned);
                    var t = JSON.stringify(saved);
                    this[i].setAttribute("mvn-data", t)
                }
            }
            return this;
        },
''',

"addSelf" : '''
        addSelf: function(){
            if(!this.prevObject){
                console.error("maven error: there is no previous object to add");
            } else {
                var t = 0;
                for(var i = this.length; t < this.prevObject.length; i++){
                    this[i] = this.prevObject[t];
                    t++;
                }
            }
            return this;
        },
'''
}

mvn_proto_end = '''
    }

    var flatten = maven.flatten = function(arr){
        var temp = [];
        function loop(atr){
            for (var i = 0; i < atr.length; i++) {
                if(Array.isArray(atr[i])){
                    loop(atr[i]);
                } else {
                    temp.push(atr[i]);
                }
            }
        }
        loop(arr);
        return temp;
    }

    var unique = maven.unique = function(arr){
        return [...new Set(arr)];
    }

    maven.id = "maven" + ( maven.fn.version + Math.random() ).replace(/\D/g,"");
    var selectar = maven.find = function(selector,context){
        context = context || document;
        var fx = {
            eq: function(i,f){
                return selectar(f,context)[i];
            },
            gt: function(n,f){
                var fmd = selectar(f,context);
                var als = [];
                n = isNaN(Number(n))?0:Number(n);
                var i = (Number(n)+1);
                while(i > n && i < fmd.length){
                    als.push(fmd[i]);
                    i++;
                }
                return als;
            },
            lt: function(n,f){
                var fmd = selectar(f,context);
                var als = [];
                n = isNaN(Number(n))?fmd.length:Number(n);
                var i = n-1;
                while(i < n && i >= 0){
                    als.push(fmd[i]);
                    i--;
                }
                return als;
            },
        },
        booleans = /(.+)(?:\:)(checked|selected|async|autofocus|autoplay|controls|defer|disabled|hidden|ismap|loop|multiple|open|readonly|required)/g,
        contexts = /(.+)(?:\:)(eq|gt|lt)\(([+|-]?\d)\)/g,
        tags = /[<](\w+)[>]/g;

        var rtd = selector;
        var elements = [];
        var types = selector.trim().split(",");
        for (var i = 0; i < types.length; i++) {
            types[i].trim()
            if(booleans.test(types[i])){
                types[i].replace(booleans,function(m,s1,s2){
                    try {
                        elements.push([...context.querySelectorAll(m)]);
                    } catch (e){
                        var els = [];
                        var als = selectar(s1,context);
                        for (var i = 0; i < als.length; i++) {
                            if(als[i][s2]) els.push(als[i]);
                        }
                    }
                });
            } else if(contexts.test(types[i])){
                types[i].replace(contexts, function(m,s1,s2,s3){
                    try {
                        elements.push([...context.querySelectorAll(m)]);
                    } catch (e){
                        if(fx[s2](s3,s1)) elements.push(fx[s2](s3,s1));
                    };
                });
            } else if(tags.test(types[i])){
                types[i].replace(tags,function(m,s1){
                    try {
                        elements.push([...context.querySelectorAll(m)]);
                    } catch (e){
                        elements.push(selectar(s1,context));
                    }
                });
            } else {
                try {
                    elements.push([...context.querySelectorAll(types[i])]);
                } catch (e){
                    console.error("maven error: out of range selector")
                }
            }
        }
        return maven.flatten([... new Set(elements)]);
    }

    start = maven.fn.start = function(selector, context){
        if(maven.next){
            this.prevObject = maven.next;
        }

        if (!selector) {
            return this;
        }
        else if(!context){
            context = document;
        }
        else if(context.ismaven){
            context = context[0];
        }
        else if(typeof context == "string"){
            context = document.querySelector(context);
        } 
        else if(context.tagName || context.nodeType){
            context = context;
        }
        else {
            context = document;
        }

        if(typeof selector == "string"){
            var elements = maven.find(selector,context);
            this.length = elements.length;
            for(var i = 0; i < elements.length; i++){
                this[i] = elements[i];
            }
        } else if(typeof selector == "function"){
            var _this = this;
            if (document.attachEvent ? document.readyState == "complete" : document.readyState != "loading") {
                selector(this);
            } else {
                document.addEventListener('DOMContentLoaded',function(e){
                    selector.call(e,_this,e)
                });
            }
        } else if(selector.ismaven){
            this.length = selector.length;
            for(var i = 0; i < selector.length; i++){
                this[i] = selector[i];
            }
        } else if(Array.isArray(selector)){
            var elements = selector;
            for(var i = 0; i < elements.length; i++){
                this[i] = elements[i];
            }
            this.length = elements.length;
        } else if(selector.tagName || selector.nodeType){
            this[0] = selector;
            this.length = 1;
        } else if(selector == document ||selector == window){
            this[0] = selector;
            this.length = 1;
        } else if(selector instanceof NodeList){
            var elements = [...selector];
            for(var i = 0; i < elements.length; i++){
                this[i] = elements[i];
            }
            this.length = elements.length;
        } else if(selector instanceof Object){
            this[0] = selector;
            this.length = 1;
        }
    
        this.selector = selector;
        maven.next = this;
        return this;
    }

    start.prototype = maven.fn;
'''

after_build_funcs =  {
"fadeToggle": '''
    function fadeToggle_(ele, dis, duration){
        this.ele = ele;
        this.dis = dis;
        this.duration = duration;
        if (dis == "none") {
            this.ele.style.opacity = "0";
            this.ele.style.display = "block";
            this.ele.style.transition = "all "+this.duration+"ms";
            setTimeout(function() {
                ele.style.opacity="1";
            }, 15);
        } else {
            this.ele.style.opacity = "1";
            this.ele.style.transition="all "+this.duration+"ms";
            setTimeout(function() {
                ele.style.opacity="0";
            }, 10);
            setTimeout(function(){
                ele.style.display="none";
            }, duration+10);
        }
    }
''',
"slideToggle": '''
    function slideToggle_(ele, dis, duration) {
        this.ele = ele;
        this.dis = dis;
        this.duration = duration;
        if (dis == "none") {
            this.ele.style.display = "block";
            this.ele.style.maxHeight = "0";
            var h = this.ele.scrollHeight + "px";
            this.ele.style.transition = "all "+this.duration+"ms";
            setTimeout(function() {
                ele.style.maxHeight = h;
            }, 10);
        } else {
            var h = this.ele.scrollHeight+"px";
            this.ele.style.maxHeight = h;
            this.ele.style.overflow = "hidden";
            this.ele.style.transition="all "+this.duration+"ms";
            setTimeout(function(){
                ele.style.maxHeight="0";
            }, 10);
            setTimeout(function() {
                ele.style.display="none";
            }, this.duration+1);
        }
    }
''',
"xss": '''
    var xss = MQuery.xss = function(str) {
        const lt = /</g;//60
        const gt = />/g;//61
        const ap = /'/g;//39
        const ic = /"/g;//34
        const st = /!/g;//33
        const sl = /\//g;//47
        const ds = /-/g;//8208
        return str.toString()
                  .replace(st, "&#33;")
                  .replace(ic, "&#34;")
                  .replace(ap, "&#39;")
                  .replace(sl, "&#47;")
                  .replace(lt, "&#60;")
                  .replace(gt, "&#61;")
                  .replace(ds, "&#8208;");
    }
''',
"ajax": '''
    var ajax = MQuery.ajax = function(url, method, data, callback, header="application/x-www-form-urlencoded; charset=UTF-8") {
        const request = new XMLHttpRequest();
        request.open(method, url, true);
        request.setRequestHeader("Content-Type", header);
        request.onload = () => {
            if (request.status >= 200 && request.status < 400) {
                const d = request.responseText;
                callback(d, request);
            } else {
                var tof;
                try {
                    var ad = request.status+" "+_ajrescd_[request.status];
                    tof = true;
                } catch(e) {
                    tof = false;
                }
                let errcod = tof ? ad : request.status;
                console.error("mquery error: The ajax request returned an error: #"+errcod);
            }
        };
        request.onerror = (message, source, lineno, colno, error) => {
            console.error("mquery error: The ajax request returned an error: "+message);
        };
        request.send(data);
    }
''',
"Import": '''
    var Import = MQuery.import = function(source, callback) {
        let script = document.createElement("script");
        const prior = document.getElementsByTagName("script")[0];
        script.async = 1;
    
        script.onload = script.onreadystatechange = (_, isAbort) => {
            if (isAbort || !script.readyState || /loaded|complete/.test(script.readyState)) {
                script.onload = script.onreadystatechange = null;
                script = undefined;
    
                if (!isAbort) {
                    if (callback) callback();
                }
            }
        };
    
        script.src = source;
        prior.parentNode.insertBefore(script, prior);
    }
''',
"parseHTML": '''
    var parseHTML = MQuery.parseHTML = function(str) {
        var tmp = document.implementation.createHTMLDocument();
        tmp.body.innerHTML = str;
        return tmp.body.children;
    };
''',
"copy": '''
    var copy = MQuery.copy = function(text) {

        let target = document.createElement("textarea");
        target.style.position = "absolute";
        target.style.left = "-9999px";
        target.style.top = "0";
        target.textContent = text;
        document.body.appendChild(target);
        target.select();
        target.setSelectionRange(0, target.value.length);

        try {
            document.execCommand("copy");
            target.remove();
        } catch (e) {
            window.prompt("Copy to clipboard: Ctrl+C, Enter", text);
        }
    }
'''
}

mvn_file_end = '''
    window.maven = window.mvn = maven;

})(this);
'''
funcs = ['add', 'toArray', 'ready', 'on', 'off', 'css', 'scroll', 'scrollTo', 'html', 'text', 'trigger', 'each', 'map', 'slice', 'find', 'filter', 'is', 'not', 'contains', 'has', 'children', 'parents', 'siblings', 'nextAll', 'prevAll', 'show', 'hide', 'empty', 'remove', 'append', 'prepend', 'after', 'before', 'addClass', 'removeClass', 'classToggle', 'hasClass', 'fadeToggle', 'slideToggle', 'val', 'len', 'submit', 'serialize', 'removeProp', 'prop', 'removeAttr', 'attr', 'data', 'addSelf']
funcs_util = ["fadeToggle", "slideToggle"]
funcs_after = ["ajax", "xss", "Import", "parseHTML", "copy"]
build = []
after_build = []
bd = []
regex = re.compile(r"^build-mavenjs\s((?:core|\*))\s?([\w+\s]{0,})$")

prompet = input("MavenJS: ")
prompet_match = re.findall(regex, prompet)
if prompet_match[0][0] == "*":
    with open('mavenjs_v1.0.2_full.js', 'w') as f:
        f.write(full)
    f.close()
    print("File generated successfully")
elif prompet_match[0][0] == "core":
    build.append(mvn_file_start)
    build.append(mvn_proto_start)
    b_funcs = prompet_match[0][1].split(" ")
    for f in b_funcs:
        if f not in funcs and f not in funcs_after:
            print(f"{f} is not a MavenJS function")
        else:
            bd.append(f)
            build.append(mvn_funcs[f])
            if f in funcs_util or f in funcs_after:
                after_build.append(after_build_funcs[f])
    build.append(mvn_proto_end)
    for fun in after_build:
        build.append(fun)
    build.append(mvn_file_end)
    code = "".join(build)
    with open(f'mavenjs_v1.0.2_{"_".join(bd)}.js', 'w') as f:
        f.write(code)
    f.close()
    print("File generated successfully")