import Template, { TemplateType } from '~/template/Template';

/**
 * A template representing a language.
 */
export default class LanguageTemplate extends Template {
    /**
     * Creates a LanuageTemplate given a language object.
     *
     * @param {Language} language - Language object
     */
    constructor(language) {
        super(
            <div class="lang-box">
                { language.icon() }
                <div class="lang-info">
                    <span class="lang-name">{ language.displayName }</span>
                    <span class="lang-desc">{ language.displayName } { language.tioId ? "supports": "does not support" } TIO.</span>
                </div>
            </div>
        );
    }
}

export class LanguageFixedTemplate extends Template {
    /**
    * @param {Language} language - Language object
     */
    constructor(language) {
        let close = <div class="close-icon"><img src="/static/img/close.svg"/></div>;

        super(
            <div class="lang-box lang-fixed">
                { language.icon() }
                <div class="lang-info">
                    <span class="lang-name">{ language.displayName }</span>
                </div>
                { close }
            </div>
        );

        this._close = close;
    }

    onDismiss(callback) {
        this._close.addEventListener("click", callback);
    }
}
