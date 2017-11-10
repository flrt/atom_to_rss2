<xsl:stylesheet
    xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
    xmlns:pyext="http://www.opikanoba.org/ns/etree-extensions"
    exclude-result-prefixes="pyext"
    extension-element-prefixes="pyext"
    version="1.0">

    <xsl:template match="/test">
        <pubDate>
            <xsl:apply-templates select="isodate" mode="RFC822"/>
        </pubDate>
    </xsl:template>

    <xsl:template match="isodate" mode="RFC822">
        <pyext:formatdt></pyext:formatdt>
    </xsl:template>
</xsl:stylesheet>
