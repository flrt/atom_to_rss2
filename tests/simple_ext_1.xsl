<xsl:stylesheet
    xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
    xmlns:atom="http://www.w3.org/2005/Atom"
    xmlns:pyext="http://www.opikanoba.org/ns/etree-extensions"
    exclude-result-prefixes="pyext"
    extension-element-prefixes="pyext"
    version="1.0">

    <xsl:import href="file://simple_ext_2.xsl"/>

    <xsl:template match="isodate">
        <pyext:formatdt></pyext:formatdt>
    </xsl:template>
</xsl:stylesheet>
